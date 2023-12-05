class A:
    def displayA(self):
        print("welcome to class A")
    
class B:
    def displayB(self):
        print("welcome to class B")
    
class C(A,B):
    def displayC(self):
        print("welcome to class C")
    
obj=C()
obj.displayA()
obj.displayB()
obj.displayC()


