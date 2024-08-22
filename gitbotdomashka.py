import telebot
from random import choice


bot = telebot.TeleBot('7153735301:AAH6ivMUIuXNyPBcVVVZRDHgA_ZpOj3yiGQ')


quotes = [
    "The only limit to our realization of tomorrow is our doubts of today. - Franklin D. Roosevelt",
    "In the end, we will remember not the words of our enemies, but the silence of our friends. - Martin Luther King Jr.",
    "The best way to predict the future is to create it. - Peter Drucker",
    "Life is what happens when you're busy making other plans. - John Lennon"
]

@bot.message_handler(commands=['quote'])
def send_quote(message):

    random_quote = choice(quotes)
    bot.reply_to(message, random_quote)


bot.polling()