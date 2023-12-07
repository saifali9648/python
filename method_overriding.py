class Ws:
    def displayinfo(self):
        print("welcome to ws cube")

class iip(Ws):
    def displayinfo(self):
        super().displayinfo()
        print("welcome to IIp")
    
obj=iip()
obj.displayinfo()
