
import telebot
class command():
    def __init__(self,Loger):
        self.functhion_name_command={}
        self.Loger=Loger
    def set(self,name:str,command):
        if not callable(command):
            raise ValueError("functhion is not callable"+str(command))
        if not isinstance(name,str):
            raise ValueError("name is not str this is:"+str(type(name)))
        self.functhion_name_command[name]=command
    def __call__(self, data):
        massage=data.text
        if not massage.startswith('/'):
            return None
        command=massage[1:].split(' ')
        if not command[0] in self.functhion_name_command:
            self.Loger.printError(ValueError(massage+" does not exist"))
            return None
        self.Loger.print(massage)
        self.functhion_name_command[command[0]](command[1:],data)



class telegrambot():
    def __init__(self,token:str,Loger):
        self._bot=telebot.TeleBot(token)
        self.commands=command(Loger.get_loger('command'))
        self.Loger=Loger
    def init(self):
        self.subscraibs(self.commands,content_types=["text"])
        self.commands.set('hi',self.hi)
    def hi(self,ms,data):
        self._bot.send_message(data.chat.id,"Привет")
    def run(self):
        try:
            self._bot.polling(interval=0)
        except Exception as Error:
            self.Loger.printError(Error)
            self.error=Error
    def subscraibs(self,functhion,*args,**kwargs):
        if not callable(functhion):
            self.Loger.printError(ValueError("functhion is not callable"+str(functhion)))
            return None

        self._bot.message_handler(*args,**kwargs)(functhion)
    def close(self):
        self._bot.close()
        del self._bot
    def iswork(self):
        try:
            user = self._bot.get_me()
            return user is not None
        except Exception as e:
            return self.error
