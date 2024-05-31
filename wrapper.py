def ERRORsenser(F):
    def Func(self,*args,**kwargs):
        try:
            F(self,*args,**kwargs)
        except Exception as Error:
            self.Loger.printError(Error)
    return Func
