class A:
    def displayA(self):
        print("welcome to class A")

class B(A):
    def displayB(self):
        print("welcome to class B")

obj=B()
obj.displayA()
obj.displayB()
