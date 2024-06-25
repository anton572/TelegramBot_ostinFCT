import conect.telegram as telegram
import conect.Flaskserver as Flaskserver
import conect.VMcontroler as VMcontroler
import argument
import threading
import Loger

def start(token):
    try:
        loger=Loger.Loger()
        telegrambot=telegram.telegrambot(token,Loger=loger.get_loger("TeleBot"))
        VM=VMcontroler.userVM(argument.vm_data,argument.P,argument.Z,argument.N,Loger=loger.get_loger("VMcontroler"))
        Flaskse=Flaskserver.Flaskserver()
        loger.print("telegrambot init")
        telegrambot.init()
        Flaskse.subscraib(loger.log_all,'/LOGER')
        telegrambot.commands.set('start_factorio',VM.StartVM)
        Flaskse.subscraib(VM.StopVM,'/stop')
        Flaskse.subscraib(VM.get_stait,'/get')
        traid=threading.Thread(target=Flaskse.run)
        traid.start()
        loger.print("telegrambot start")
        telegrambot.run()
    finally:
        telegrambot._bot.close()
        del traid
if __name__ == '__main__s':
    start(argument.token)
