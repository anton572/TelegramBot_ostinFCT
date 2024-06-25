import conect.telegram as telegram
import conect.Flaskserver as Flaskserver
import conect.VMcontroler as VMcontroler
import argument
import threading
import Loger

def start(token):
    try:
        loger=Loger.Loger()
        print(argument.token)
        telegrambot=telegram.telegrambot(token,Loger=loger.get_loger("TeleBot"))
        VM=VMcontroler.userVM(argument.P,argument.Z,argument.N,Loger=loger.get_loger("VMcontroler"))
        Flaskse=Flaskserver.Flaskserver()
        loger.print("telegrambot init")
        telegrambot.init()
        Flaskse.subscraib(loger.log_all,'/LOGER')
        VM.StartVM()
        telegrambot.commands.set('start_factorio',VM.StartVM)
        Flaskse.subscraib(VM.StopVM,'/stop')
        Flaskse.subscraib(VM.get_stait,'/get')
        traid=threading.Thread(target=Flaskse.run)
        traid.start()
        loger.print("telegrambot start")
        telegrambot.run()
        while True:
            pass
    finally:
        telegrambot._bot.close()
        del traid
if __name__ == '__main__':
    start(argument.token)
