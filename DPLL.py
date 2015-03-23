__author__ = 'Guruguha'

import sys
import random


def main(args):
    """
    Start routine for the program
    :param args: arguments have the option -i and input file name
    :return: NA, write Satisfiability assignments of read sentences to an output file
    """

    """ Read the input file data """
    sentences = read_file_data(args)

    """ Start routine to run SAT solver """
    satisfiability = find_satisfiability(sentences)

    sat_op_file = open('CNF_satisfiability.txt', 'w');
    for sat in satisfiability:
        sat_op_file.write(str(sat))
        sat_op_file.write("\n")
    sat_op_file.close()


def read_file_data(args):
    """
    Opens the input file in args and reads data
    :param args: arguments to open a file -- option and filename
    :return: input CNF sentences
    """

    lines = []
    line_cnt = 0
    num_lines = 0
    if args[1] == "-i":
        if args[2] != "":

            """ Open input file """
            with open(args[2], 'r') as file_data:
                for line in file_data:
                    if line_cnt == 0:
                        num_lines = int(line)
                    line_cnt += 1
                    lines.append(line)

            if line_cnt != num_lines + 1:
                print "Check file format... Check number of input lines provided."
                sys.exit()
        else:
            print "No file provided"
            sys.exit()
    else:
        print "Invalid or no option provided"
        sys.exit()

    return lines[1:]


def find_satisfiability(sentences):
    """
    :param sentences: set of sentences read from input file
    :return: a satisfiable assignment if any exists, false otherwise
    """

    satisfiability = []
    for sentence in sentences:
        satisfiability.append(apply_dpll(eval(sentence)))

    return satisfiability


def apply_dpll(sentence):
    """
    :param sentence: CNF sentence on which DPLL algorithm is applied
    :return: a satisfiable assignment if any exists, false otherwise
    """

    set_of_clauses = get_clauses(sentence)
    literal_symbols = find_literal_symbols(sentence)
    sat_assignment = dpll(set_of_clauses, literal_symbols, {})

    if sat_assignment:
        sat = format_satisfiability(sat_assignment)
    else:
        sat = ["false"]

    return sat


def format_satisfiability(sat_assignment):
    """
    :param sat_assignment: a SAT assignment to one of the input CNF sentences
    :return: list formatted SAT assignment
    """

    final_sat = ["true"]
    for key, val in sat_assignment.iteritems():
        key_val_str = str(key).upper() + "=" + str(val).lower()
        final_sat.append(key_val_str)

    return final_sat


def dpll(clauses, literals, model):
    """
    :param clauses: set of clauses of the input sentence
    :param literals: set of literals of the input sentence
    :param model: set of truth value assignments for each literal in literals
    :return: model, set of truth value assignments
    """

    """ Set of clauses with no truth value assigned """
    unknown_clauses = []
    for clause in clauses:
        truth_assgt = get_truth_values(clause, model)
        if truth_assgt == False:
            return False
        if truth_assgt != True:
            unknown_clauses.append(clause)

    if not unknown_clauses:
        if literals:
            """ If some literal doesn't have truth value assignment, assign random truth value """
            model = apply_random_assignments(literals, model)
        return model

    """ Find a pure symbol if available """
    pure_symbol, ps_val = find_pure_symbol(literals, unknown_clauses)
    if pure_symbol:
        return dpll(clauses, remove_symbol(pure_symbol, literals), update_model(model, pure_symbol, ps_val))

    """ Find a unit clause if available """
    unit_clause, uc_val = find_unit_clause(clauses, model)
    if unit_clause:
        return dpll(clauses, remove_symbol(unit_clause, literals), update_model(model, unit_clause, uc_val))

    next_literal = literals.pop()
    return (dpll(clauses, literals, update_model(model, next_literal, True)) or
            dpll(clauses, literals, update_model(model, next_literal, False)))


def apply_random_assignments(literals, model):
    """
    :param literals: literals with no truth value assigned
    :param model: set of literats and a valid truth value assignment for each
    :return: updated model with all literals assigned a truth value
    """

    updated_model = {}
    for literal in literals:
        truth_val = bool(random.getrandbits(1))
        updated_model = update_model(model, literal, truth_val)
        model = updated_model
    return updated_model


def remove_symbol(symbol, literals):
    """
    :param symbol: literal to be removed from literals
    :param literals: literals with no truth value assigned
    :return: updated literals with no truth value assigned
    """

    if isinstance(symbol, list):
        for literal in literals:
            if isinstance(literal, list):
                if literal[0] == "not":
                    if literal[1] == symbol[1]:
                        literals.remove(symbol)
    else:
        literals.remove(symbol)

    return literals


def find_pure_symbol(literals, unknown_clauses):
    """
    :param literals: set of all literals in the given sentence and no truth value assigned
    :param unknown_clauses: set of all clauses with no truth value assignment yet
    :return: a pure symbol and its value if found, None otherwise
    """

    for literal in literals:
        literal_found = False
        literal_neg_found = False

        for clause in unknown_clauses:
            found = find_literal(literal, clause)
            if not literal_found and found:
                literal_found = True

            if isinstance(literal, list):
                find_this = literal[1]
            else:
                find_this = ["not", literal]

            found = find_literal(find_this, clause)
            if not literal_neg_found and found:
                literal_neg_found = True

        if literal_found != literal_neg_found:
            return literal, literal_found

    return None, None


def find_unit_clause(clauses, model):
    """
    :param clauses: set of remaining clauses with no truth value assigned yet
    :param model: set of literals with valid truth value assigned
    :return: a unit clause and its value if found, None otherwise
    """

    for clause in clauses:
        num_absent_in_model = 0
        not_literal = False
        for sub_clause in get_sub_clauses_of(clause):
            if sub_clause == "not":
                not_literal = True
                continue

            if not_literal:
                sub_clause = ["not", sub_clause]

            symbol = literal_symbol(sub_clause)

            if symbol not in model:
                num_absent_in_model += 1
                unit_clause, val = symbol, sub_clause[0] != "not"

        if num_absent_in_model == 1:
            return unit_clause, val

    return None, None


def literal_symbol(clause):
    """
    :param clause: a clause with a set of literals
    :return: a literal of the clause
    """

    if clause[0] == "not":
        return clause[1]
    else:
        return clause


def find_literal(find_this, in_clause):
    """
    :param find_this: symbol to be found
    :param in_clause: search for "find_this" in in_clause
    :return: True if literal found, False otherwise
    """

    if isinstance(in_clause, list):
        if in_clause[0] == "not":
            if isinstance(find_this, list):
                if in_clause[1] == find_this[1]:
                    return True
        else:
            for sub_clause in in_clause:
                if isinstance(sub_clause, list):
                    if sub_clause[0] == "not":
                        if isinstance(find_this, list):
                            if sub_clause[1] == find_this[1]:
                                return True
                elif isinstance(sub_clause, str):
                    if sub_clause == find_this:
                        return True
    elif isinstance(in_clause, str):
        if in_clause == find_this:
            return True

    return False


def get_sub_clauses_of(clause):
    """
    :param clause: main clause
    :return: a sub-clause of param clause
    """

    if isinstance(clause, list):
        if clause[0] == "or":
            return clause[1:]
        elif clause[0] == "not":
            return clause
    else:
        return clause


def get_truth_values(clause, model):
    """
    :param clause: clause for which truth value is to be found
    :param model: set of literals with valid truth value assignments
    :return: True/False if truth value is found, None otherwise
    """

    if isinstance(clause, list):
        sub_clause_notation = clause[0]
        sub_clause_rest = clause[1:]

        if sub_clause_notation == "and":
            truth_val = True
            for elem in sub_clause_rest:
                truth_val_of_elem = get_truth_values(elem, model)
                if truth_val_of_elem == False:
                    return False
                if truth_val_of_elem == None:
                    truth_val = None
            return truth_val
        elif sub_clause_notation == "or":
            truth_val = False
            for elem in sub_clause_rest:
                truth_val_of_elem = get_truth_values(elem, model)
                if truth_val_of_elem == True:
                    return True
                if truth_val_of_elem == None:
                    truth_val = None
            return truth_val
        elif sub_clause_notation == "not":
            truth_val = get_truth_values(sub_clause_rest[0], model)
            if truth_val == None:
                return None
            else:
                return not truth_val
        elif check_if_literal(sub_clause_notation[0]):
            return model.get(sub_clause_rest[0])
    elif isinstance(clause, str):
        if check_if_literal(clause):
            return model.get(clause)


def get_clauses(sentence):
    """
    :param sentence: CNF sentence with a set of clauses
    :return: all clauses of the input sentence
    """

    if isinstance(sentence, list) and sentence[0] == "and":
        return sentence[1:]
    else:
        return [sentence]


def find_literal_symbols(sentence):
    """
    :param sentence: CNF sentence with a set of clauses
    :return: set of all literals of the input sentence
    """

    if isinstance(sentence, list):
        set_of_literals = []
        for sub_val in sentence[1:]:
            if sub_val[0] == "not":
                if sub_val[1] not in set_of_literals:
                    set_of_literals.append(sub_val[1])
            else:
                for symbol in find_literal_symbols(sub_val):
                    if symbol not in set_of_literals:
                        set_of_literals.append(symbol)
        return set_of_literals
    else:
        if check_if_literal(sentence):
            return [sentence]


def check_if_literal(expr):
    """
    :param expr: expression with a set of literals or a literal (ex: A, B, ...)
    :return: True if expr is a literal, False otherwise
    """

    return len(expr) == 1 and isinstance(expr[0], str)


def update_model(old_model, literal, truth_val):
    """
    :param old_model: model that is to be updated
    :param literal: literal for which truth value is found
    :param truth_val: truth value of input param literal
    :return: updated model with literal and its truth value in it
    """

    new_model = old_model.copy()
    if isinstance(literal, list):
        if literal[0] == "not":
            new_literal = str(literal[0]) + str(literal[1])
        new_model[new_literal] = truth_val
    else:
        new_model[literal] = truth_val

    return new_model


if __name__ == "__main__":
    main(sys.argv)

