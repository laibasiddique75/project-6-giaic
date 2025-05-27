class A:
    def show(self):
        print("Show from A")

class B(A):
    def show(self):
        print("Show from B")

class C(A):
    def show(self):
        print("Show from C")

class D(B, C):  # Diamond Inheritance
    pass

# Create object of D and call show
d = D()
d.show()

# Print the Method Resolution Order
print(D.__mro__)
