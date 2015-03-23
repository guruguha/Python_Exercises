__author__ = 'Guruguha'
import sys

and_present = False
cnf_sentences = []


def main(args):
    """
    Start routine for the program
    :param args: arguments have the option -i and input file name
    :return: NA, write converted CNF sentences of read sentences to an output file
    """

    lines = read_file_data(args)
    parse_data(lines)

    op_file = open('sentences_CNF.txt', 'w');
    for sentence in cnf_sentences:
        op_file.write(str(sentence))
        op_file.write("\n")
    op_file.close()


def read_file_data(args):
    """
    Opens the input file in args and reads data
    :param args: arguments to open a file -- option and filename
    :return: input propositional sentences
    """

    lines = []
    line_cnt = 0
    num_lines = 0
    if args[1] == "-i":
        if args[2] != "":
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

    return lines


def parse_data(data):
    """
    :param data: propositional sentences read from file
    :return: NA
    """

    for itr in range(1, len(data)):
        list_data = eval(data[itr])
        convert_to_cnf(list_data)


def convert_to_cnf(sentence):
    """
    :param sentence: propositional sentence to be converted to CNF
    :return: NA, update cnf_sentences list with latest converted sentence
    """

    flat_expr = convert(
        apply_distributive_law(negate_expr(get_implies_free_expr(get_double_implies_free_expr(sentence)))))

    final_cnf_expr = []
    global and_present
    if and_present:
        for list_val in flatten_and_expr(flat_expr):
            final_cnf_expr.append(list_val)
    else:
        final_cnf_expr = flat_expr[0:]
    final_expr = []
    if and_present:
        and_present = False
        final_expr.append("and")
    no_dup_expr = remove_duplicates(final_cnf_expr)
    for exp in no_dup_expr:
        final_expr.append(exp)

    print(final_expr)
    cnf_sentences.append(final_expr)


def remove_multiple_ands(expr):
    notation = expr[0]
    if notation == "and":
        return [remove_multiple_ands(expr[1]), remove_multiple_ands(expr[2])]
    else:
        return expr


def get_double_implies_free_expr(sentence):
    """
    :param sentence: propositional sentence that might contain double implications (ex: A <==> B)
    :return: propositional sentence without double implications (ex: A ==> B and B ==> A)
    """

    no_double_implies_expr = []

    if isinstance(sentence, list):
        notation = sentence[0]
        if notation != "not":
            left_expr = get_double_implies_free_expr(sentence[1])
            right_expr = get_double_implies_free_expr(sentence[2])
            if notation == "iff":
                no_double_implies_expr.append("and")
                left_sub_expr = ["implies", left_expr, right_expr]
                right_sub_expr = ["implies", right_expr, left_expr]
                no_double_implies_expr.append(left_sub_expr)
                no_double_implies_expr.append(right_sub_expr)
            else:
                no_double_implies_expr.append(notation)
                no_double_implies_expr.append(left_expr)
                no_double_implies_expr.append(right_expr)
        else:
            expr = get_double_implies_free_expr(sentence[1])
            no_double_implies_expr.append("not")
            no_double_implies_expr.append(expr)
    elif isinstance(sentence, str):
        no_double_implies_expr = sentence

    return no_double_implies_expr


def get_implies_free_expr(sentence):
    """
    :param sentence: propositional sentence which might contain an implication expression (ex: A ==> B)
    :return: propositional sentence with implications removed (ex: not A or B)
    """

    no_implies_expr = []
    if isinstance(sentence, list):
        notation = sentence[0]
        if notation != "not":
            left_sub = get_implies_free_expr(sentence[1])
            right_sub = get_implies_free_expr(sentence[2])
            if notation == "implies":
                no_implies_expr.append("or")
                left_sub_tree = ["not", left_sub]
                no_implies_expr.append(left_sub_tree)
                no_implies_expr.append(right_sub)
            else:
                no_implies_expr.append(notation)
                no_implies_expr.append(left_sub)
                no_implies_expr.append(right_sub)
        else:
            expr = get_implies_free_expr(sentence[1])
            no_implies_expr.append("not")
            no_implies_expr.append(expr)
    elif isinstance(sentence, str):
        no_implies_expr = sentence

    return no_implies_expr


def negate_expr(expr):
    """
    :param expr: an expression with negation not with the literal but with the expression or sub-expression itself (ex: not (A or B))
    :return: an expression with negation moved down to the literal (ex: not A and not B)
    """

    if isinstance(expr, list):
        notation = expr[0]
        if notation == "not":
            right_sub_expr = expr[1]
            if isinstance(right_sub_expr, list):
                sub_notation = right_sub_expr[0]
                if sub_notation == "not":
                    negated_expr = negate_expr(right_sub_expr[1])
                else:
                    left_expr = negate_expr(["not", right_sub_expr[1]])
                    right_expr = negate_expr(["not", right_sub_expr[2]])
                    if sub_notation == "or":
                        negated_expr = ["and", left_expr, right_expr]
                    elif sub_notation == "and":
                        negated_expr = ["or", left_expr, right_expr]
            elif isinstance(right_sub_expr, str):
                negated_expr = ["not", right_sub_expr]
        else:
            left_expr = negate_expr(expr[1])
            right_expr = negate_expr(expr[2])
            negated_expr = [notation, left_expr, right_expr]
    elif isinstance(expr, str):
        negated_expr = expr

    return negated_expr


def apply_distributive_law(expr):
    """
    :param expr: an expression with only or, and and not notations
    :return: an expression after applying distributive law
    """

    if isinstance(expr, list):
        if expr[0] == "not":
            temp_expr = expr
        else:
            notation = expr[0]
            left_expr = apply_distributive_law(expr[1])
            right_expr = apply_distributive_law(expr[2])

            if notation == "or":
                temp_expr = distribute_or_on_expr(left_expr, right_expr)
            else:
                temp_expr = ["and", left_expr, right_expr]
    else:
        temp_expr = expr

    return temp_expr


def distribute_or_on_expr(expr1, expr2):
    """
    :param expr1: left sub-expression of a bigger expression
    :param expr2: right sub-expression of a bigger expression
    :return: an expression after applying distributive law
    """

    if isinstance(expr1, list) and expr1[0] == "and":
        final_expr = ["and", distribute_or_on_expr(expr1[1], expr2), distribute_or_on_expr(expr1[2], expr2)]
    elif isinstance(expr2, list) and expr2[0] == "and":
        final_expr = ["and", distribute_or_on_expr(expr1, expr2[1]), distribute_or_on_expr(expr1, expr2[2])]
    else:
        final_expr = ["or", expr1, expr2]

    return final_expr


def get_conjuncts_of_disjuncts(expr):
    """
    :param expr: expression not in CNF
    :return: and expression/sentence in CNF
    """

    if isinstance(expr, list):
        notation = expr[0]
        if notation == "not":
            return expr
        elif notation == "or":
            return [get_conjuncts_of_disjuncts(expr[1]), get_conjuncts_of_disjuncts(expr[2])]
    else:
        return expr


def convert(expr):
    """
    :param expr: and expression/sentence not in CNF
    :return: and expression/sentence in CNF
    """

    converted_expr = []
    if isinstance(expr, list):
        if expr[0] == "not":
            converted_expr = expr
        else:
            notation = expr[0]
            if notation == "or":
                left_expr = get_conjuncts_of_disjuncts(expr[1])
                right_expr = get_conjuncts_of_disjuncts(expr[2])

                converted_expr = [notation, left_expr, right_expr]

                flat_expr = []
                for list_val in flatten_expr(converted_expr):
                    flat_expr.append(list_val)
                converted_expr = flat_expr
            else:
                global and_present
                and_present = True
                converted_expr = [convert(expr[1]), convert(expr[2])]
    else:
        converted_expr = expr

    return converted_expr


def flatten_expr(expr):
    """
    :param expr: an expression that might contain multiple AND
    :return: a flattened expression
    """

    for list_val in expr:
        if isinstance(list_val, list):
            if list_val[0] == "not":
                yield list_val
            else:
                for sub_list_val in flatten_expr(list_val):
                    yield sub_list_val
        else:
            yield list_val


def flatten_and_expr(expr):
    """
    :param expr: non-flattened expression
    :return: flattened expression with only ond AND symbol
    """
    for list_val in expr:
        if isinstance(list_val, list):
            if list_val[0] == "not" or list_val[0] == "or":
                yield list_val
            else:
                for sub_list_val in flatten_and_expr(list_val):
                    yield sub_list_val
        else:
            yield list_val


def remove_duplicates(expr):
    """
    :param expr: an expression with possible duplicates
    :return: expression with no duplicates
    """

    no_dup_expr = []

    for sub_expr in expr:
        sub_list = remove_duplicate(sub_expr)
        no_dup_expr.append(sub_list)

    return no_dup_expr


def remove_duplicate(expr):
    """
    Helper function for remove_duplicates function
    :param expr: expression with a duplicate
    :return: expression without a duplicate
    """

    if not expr:
        no_dup = expr
    else:
        if isinstance(expr, list):
            if len(expr) > 1:
                tmp = expr[1]
                rem = remove_duplicate(expr[2:])
                if tmp in rem:
                    no_dup = [expr[0]]
                    for elem in rem:
                        no_dup.append(elem)
                else:
                    no_dup = [expr[0], tmp]
                    for elem in rem:
                        no_dup.append(elem)
            else:
                no_dup = expr
        else:
            no_dup = expr

    return no_dup


if __name__ == "__main__":
    main(sys.argv)