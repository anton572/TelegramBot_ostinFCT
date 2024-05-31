import conect.telegram as telegram
import conect.Flaskserver as Flaskserver
import on_off_server
import argument
import threading
import Loger

def start(token):
    try:
        loger=Loger.Loger()
        telegrambot=telegram.telegrambot(token,Loger=loger.get_loger("TeleBot"))
        server=on_off_server.server(argument.Token_WEB,argument.Start_WEB,argument.Stop_WEB,Loger=loger.get_loger("ServControl"))
        Flaskse=Flaskserver.Flaskserver()
        loger.print("telegrambot init")
        telegrambot.init()

        telegrambot.commands.set('start_factorio',server.strart)

        traid=threading.Thread(target=Flaskse.run)
        traid.start()
        loger.print("telegrambot start")
        telegrambot.run()
    finally:
        del traid

if __name__ == '__main__':
    start(argument.token)
