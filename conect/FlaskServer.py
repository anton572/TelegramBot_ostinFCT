from flask import Flask
class FlaskServer():
    def __init__(self,Loger):
        self.app=Flask('')
        self.Loger=Loger
        self.run=self.LOG_arg(self.run,'run FlaskServer')
    def LOG_arg(self,F,P):
        def func(*args,**kwargs):
            try:
                self.Loger.print(P+" - invaite")
                arg=F(*args,**kwargs)

            except Exception as Error:
                self.Loger.printError(Error)
            return arg
        func.__name__=F.__name__
        return func
    def init(self):
        self.subscraibs(self.home,'/')
        self.subscraibs(self.is_live,'/iot',methods=["GET"])
    def home(self):
        return "live"
    def is_live(self):
        return "iot_alive"
    def subscraibs(self,functhion,path:str,*args,**kwargs):
        meth=self.LOG_arg(functhion,path)
        print(meth)
        self.app.route(path,*args,**kwargs)(meth)

    def run(self):
        self.app.run(host='0.0.0.0',port=80)


