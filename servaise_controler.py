import threading,time
class servaise():
    def __init__(self,servais):
        self.__servais=servais

        self.instans=None
    def start(self,*args,**kwargs):
        self._args=args
        self._kwargs=kwargs
        self.instans=self.__servais(*args,**kwargs)
    def run(self):
        self.__work=True
        path=threading.Thread(target=self._sran)
        path.run()
    def get_instans(self):
        return self.instans
    def stop(self):
        self.__work=False
        self.instans.stop()
    def _sran(self):
        while self.__work:
            try:
                self.instans.init()
                self.instans.run()
            except:
                if self.__work:
                    self.stop()
                    time.sleep(100)
                    self.__servais.__init__(self.instans,*self._args,**self._kwargs)



