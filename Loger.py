import datetime
class ALoger():
    def print(self,log)->None:
        pass
    def get_loger(self,name):
        pass
    def printError(self,Error:Exception):
        self.print("<Error>{}; Args:{}".format(type(Error).__name__,str(Error.args)))
class Loger(ALoger):

    def __init__(self):
        self.name="serv.log"
    def print(self,log)->None:
        data=datetime.datetime.now().strftime("[%H:%M:%S-%d.%m.%Y]")
        self.__write(data+str(log))
    def __write(self,mas):
        print(mas)
        t=open(self.name,'a')
        t.write(mas+"\n")
        t.close()
    def get_loger(self,name)->ALoger:
        return DownLoger(name,self)
    def close(self):
        pass
class DownLoger(ALoger):
    def __init__(self,name,Loger):
        self.__name=name
        self.__Loger=Loger
    def print(self,log)->None:
        masg="[{}]{}".format(self.__name,log)
        self.__Loger.print(masg)
    def get_loger(self,name)->ALoger:
        return DownLoger(name,self)
