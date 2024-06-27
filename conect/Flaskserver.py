from flask import Flask,redirect
class Flaskserver():
    def __init__(self):
        self.app=Flask("host")
        self.subscraib(self.respons,'/resp/<M>')
    def respons(self,M):
        return M
    def run(self):
        self.app.run(host='0.0.0.0',port=80)
    def subscraib(self,F,path,**options):
        self.app.route(path,**options)(F)
    @staticmethod
    def reline(link):
        return redirect(link)
