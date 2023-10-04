# имя бота CoddySergey

# никнейм бота CoddySergeyBot
# ссылка на бота https://t.me/CoddySergeyBot

# TOKEN = 6545234588:AAHet3AGYDl8zRmCp0yrVNfcdIxFBnai0co

import telebot
from time import sleep

from telebot import types
import random

import webbrowser
import sqlite3


TOKEN = "6545234588:AAHet3AGYDl8zRmCp0yrVNfcdIxFBnai0co"

# библиотека telebot содержит класс TeleBot

# обьект     = библиотека.класс(свойство)
moySuperBot = telebot.TeleBot(TOKEN)
# вся документация по апи тут
# https://core.telegram.org/bots/api

def wait(time):
    moySuperBot.send_chat_action(message.chat.id, "typing")  # typing
    sleep(time)

# обработчик команды /start
@moySuperBot.message_handler(commands=["start"])
def obrabotchikKomandiStart(message):
    ########
    # 2 встроенная клавиатура
    ########
    raskladka1 = types.ReplyKeyboardMarkup(resize_keyboard=True)
    levayaKnopka = types.KeyboardButton("кинуть кубик")
    pravayaKnopka = types.KeyboardButton("Ну как дела ☺?")
    raskladka1.add(levayaKnopka, pravayaKnopka)

    sti = open("hello.webp", "rb")  # add sticker obj
    moySuperBot.send_sticker(message.chat.id, sti)  # send sticker
    moySuperBot.send_chat_action(message.chat.id, "typing")  # typing
    sleep(2.5)

    # moySuperBot.send_message(комуОтправить, какоеСообщениеОтправить)
    moySuperBot.send_message(
        message.chat.id,
        "Привет, {0.first_name}. \n Это <b>{1.first_name}</b> бот. Меня создал Алехин Сергей.".format(
            message.from_user, moySuperBot.get_me()
        ),
        parse_mode="html",
        reply_markup=raskladka1,
    ) 
    

##########
# 4 обработка /show
##########
@moySuperBot.message_handler(commands=["show"])
def kommandaShow(message):
    # 4.1 посмотрим весь обьект message
    moySuperBot.send_message(message.chat.id, message)


############### 4.2 самостоятельная работа
@moySuperBot.message_handler(commands=["myid"])
def kommandaMyid(message):
    moySuperBot.send_message(message.chat.id, message.from_user.id)
    moySuperBot.reply_to(message, f"твой ID {message.from_user.id}")

