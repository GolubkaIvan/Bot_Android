import telebot
import config

bot = telebot.TeleBot(config.TOKEN)
 #Старт
@bot.message_handler(commands=['start'])
def start_message(message):
    bot.send_message(message.chat.id, "Привет, {0.first_name}. Чтобы посмотреть список команд введите /help ".
    format(message.from_user, bot.get_me()), parse_mode='html')
    if message.text == 'Да это жестко':
        audio1 = open('daeto.ogg', 'rb')
        bot.send_audio('-1001454317343', audio1)
         

 #Команда /help
@bot.message_handler(commands=['help'])
def help_message(message):
    bot.send_message(message.chat.id, "/polnomochie - Тут это самое наши полномочия все. /ahaha - Ты меня расмешнил. /eboy - Ахаха е бой. /daeto - Да это жестко!")

  
    
    #Фразочки
@bot.message_handler(commands=['polnomochie'])
def play_music(message):
    audio = open('audio.ogg', 'rb')
    bot.send_audio('-1001454317343', audio)
    
@bot.message_handler(commands=['ahaha'])
def play_music(message):
    audio = open('ahah.ogg', 'rb')
    bot.send_audio('-1001454317343', audio)
    
@bot.message_handler(commands=['daeto'])
def play_music(message):
    audio = open('daeto.ogg', 'rb')
    bot.send_audio('-1001454317343', audio)

@bot.message_handler(commands=['eboy'])
def play_music(message):
    audio = open ('mp.mp4', 'rb')
    bot.send_video('-1001454317343', audio)    

bot.polling(none_stop=True, interval=0)



    