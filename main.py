import telebot
import time
from  bot_token import token as tk

bot = telebot.TeleBot(tk) # Вместо tk используй свой токен тг бота

@bot.message_handler(commands=['start'])
def first_use(message):
    bot.send_message(message.from_user.id, 'Привет, мой псевдоним artsiompichinko. Я пишу на Python 3.\n'
                                           'В этом боте можно узнать информацию о моих работах и сделать заказ. '
                                           'Так можно найти мои контакты и оставить заявку на обратную связь')

if __name__ == '__main__':
    while True:
        try:
            bot.polling(none_stop=True)
        except Exception as e:
            print(e)
            time.sleep(15)