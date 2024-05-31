import requests
import wrapper
class server():
    def __init__(self,get_token,start,stop,Loger):
        self.__token = requests.request('GET',get_token)
        self.__start,self.__stop=start,stop
        self.Loger=Loger
    @wrapper.ERRORsenser
    def strart(self):
        requests.request('POST',self.__start,params=self.__token)
    @wrapper.ERRORsenser
    def stop(self):
        requests.request('POST',self.__stop,params=self.__token)
