#   inheritence types
# single
# multi level
# multiple inheritence


# .....single
class A():
    def method_a(self):
        print("Method A")

class B(A):
    def method_b(self):
        print("Method B")

emp_1 = B()
emp_1.method_a()



# .....multi level
class A():
    def method_a(self):
        print("Method A")
    def show(self):
        print("grand parent")

class B(A):
    def method_b(self):
        print("Method B")
    def show(self):
        print("parent")

class C(B):
    def method_c(self):
        print("Method C")
    def show(self):
        print("child")
emp_1 = C()
emp_1.method_a()
emp_1.show()


# .....multiple inheritence
class A():
    def method_a(self):
        print("Method A")

class B():
    def method_b(self):
        print("Method B")

class C(A, B):
    def method_c(self):
        print("Method C")
emp_1 = C()
emp_1.method_a()