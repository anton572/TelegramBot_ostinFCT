import conect.telegram as telegram
import conect.Flaskserver as Flaskserver
import conect.VMcontroler as VMcontroler
import argument
import threading
import Loger
from servaise_controler import servaise
def start(token):
    try:
        loger=Loger.Loger()
        telegrambot=telegram.telegrambot(token,Loger=loger.get_loger("TeleBot"))
        telegrambot.init()
        VM=VMcontroler.userVM(argument.P,argument.Z,argument.N,Loger=loger.get_loger("VMcontroler"))
        Flaskse=Flaskserver.Flaskserver()
        Flaskse.subscraib(lambda :loger.log_all().replace('\n','<div>'),'/LOGER')
        telegrambot.commands.set('start_factorio',lambda *a,**k:VM.StartVM())
        def stop():
            VM.StopVM()
            return Flaskse.reline("/get")
        Flaskse.subscraib(stop,'/stop')
        Flaskse.subscraib(VM.get_stait,'/get')
        traid=threading.Thread(target=Flaskse.run)
        traid.start()
        loger.print("telegrambot start")
        telegrambot.run()

    finally:
        telegrambot.stop()
        del traid
if __name__ == '__main__':
    start(argument.token)
