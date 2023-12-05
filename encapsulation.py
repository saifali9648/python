class studetns:
    def __init__(self):
        self.__name=""
    def getname(self):
        return self.__name
    def setname(self,name):
        self.__name=name
    
obj=studetns()
obj.setname("saif")
name=obj.getname()
print(name)