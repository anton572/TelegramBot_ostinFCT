import conect.telegram as telegram
import conect.FlaskServer as FlaskServer
import on_off_server
import argument
import threading
import Loger

def start(token):
    try:
        loger=Loger.Loger()
        telegrambot=telegram.telegrambot(token,Loger=loger.get_loger("TeleBot"))
        beck=FlaskServer.FlaskServer(Loger=loger.get_loger("Beck"))
        server=on_off_server.server('https://www.youtube.com/','https://','https://',Loger=loger.get_loger("ServControl"))

        loger.print("telegrambot init")
        telegrambot.init()
        loger.print("beck init")
        beck.init()

        def iswork():
            return {'work':telegrambot.iswork()}
        telegrambot.commands.set('start_factorio',server.strart)
        beck.subscraibs(iswork,'/isworktelegrambot')


        trase=threading.Thread(target=beck.run)
        loger.print("beck start")
        trase.start()
        loger.print("telegrambot start")
        telegrambot.run()
    finally:
        del trase
        loger.close()

if __name__ == '__main__':
    start(argument.token)
