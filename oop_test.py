from abc import abstractmethod, ABCMeta


class NewClass:
    z = 100

    def __init__(self):
        self.x = 10
        self.y = 23

    def some_method(self, rr):
        print("something " + str(self.x + rr))

    def print_method(self):
        print(NewClass.z)


class SubClass(NewClass):
    child_var = 20

    def print_method(self):
        print("child")

    @classmethod
    def static_method(cls):
        print(SubClass.child_var)
obj = NewClass()
obj2 = NewClass()
NewClass.z += 10
print(getattr(obj, 'x'))

sub = SubClass()
sub.print_method()
sub.some_method(12121)

SubClass.static_method()


class Vector:
    __metaclass__ = ABCMeta
    x = 9

    def __init__(self, a, b):
        self.a = a
        self.b = b
    #
    # def __str__(self):
    #     return "Vector (%d, %d) " % (self.a, self.b)
    #
    # def __add__(self, other):
    #     return Vector(self.a + other.a, self.b + other.b)

    @abstractmethod
    def some_method(self):
        pass


class SubVector(Vector):

    sum = 1000

    def __init__(self, a):
        super(SubVector,self).__init__(10, a)
        self.p = a

    # def some_method(self):
    #     print("helloooo")
    #     print(self.a)
    #     print(self.p)

subVector = SubVector(1)
subVector.some_method()
