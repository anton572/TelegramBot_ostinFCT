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
        TS=servaise(telegram.telegrambot)
        TS.start(token,Loger=loger.get_loger("TeleBot"))
        telegrambot= TS.get_instans()
        VM=VMcontroler.userVM(argument.P,argument.Z,argument.N,Loger=loger.get_loger("VMcontroler"))
        Flaskse=Flaskserver.Flaskserver()
        Flaskse.subscraib(loger.log_all,'/LOGER')
        telegrambot.commands.set('start_factorio',lambda *a,**k:VM.StartVM())
        Flaskse.subscraib(VM.StopVM,'/stop')
        Flaskse.subscraib(VM.get_stait,'/get')
        traid=threading.Thread(target=Flaskse.run)
        traid.start()
        loger.print("telegrambot start")
        TS.run()
        while True:
            pass
    finally:
        TS.stop()
        del traid
if __name__ == '__main__':
    start(argument.token)
