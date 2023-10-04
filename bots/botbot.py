# имя бота CoddySergey
# тут был Дамир
# никнейм бота CoddySergeyBot
# ссылка на бота https://t.me/CoddySergeyBot

# TOKEN = 6545234588:AAHet3AGYDl8zRmCp0yrVNfcdIxFBnai0co
# имя бота coddyDamir
# никнейм бота coddyDamir
# ссылка на бота 
# рандом библиотека
import random
# token = 
import telebot
from telebot import types
# импортирем из библиотека time метод sleep 
from time import sleep
import webbrowser


TOKEN = "6545234588:AAHet3AGYDl8zRmCp0yrVNfcdIxFBnai0co"

#библиотека телебот содержить класс TeleBot

#обект = библиотека.класс(свойства)
mySuperBot = telebot.TeleBot(TOKEN)

#обработчик команды /start
@mySuperBot.message_handler(commands=['start'])
def obrabotkaKomandiStart(message):
    # mySuperBot.send_message(комуОтправить, какое собщениеОтправить)
    sti = open('hello.webp', 'rb')
    mySuperBot.send_sticker(message.chat.id, sti)
    mySuperBot.send_chat_action(message.chat.id, 'typing')
    
    # создаём кливиутуру с кнопками
    raskladka1 = types.ReplyKeyboardMarkup (resize_keyboard=True)
    leftbutton = types.KeyboardButton("Ну как дела")
    rightbutton = types.KeyboardButton("Кинут кубик")
    leftbutton1 = types.KeyboardButton("Как настроение")
    rightbutton1 = types.KeyboardButton("Кто ты?")
    raskladka1.add(leftbutton, rightbutton, leftbutton1, rightbutton1)
    sleep(2)
    mySuperBot.send_message(message.chat.id, "Привет,  {0.first_name}. \n Это <b> {1.first_name} </b> бот. Меня создал Дамир".format(message.from_user, mySuperBot.get_me()), parse_mode='html', reply_markup=raskladka1)

#обработчик команды /bye
@mySuperBot.message_handler(commands=['bye']) 
def obrabotkaKomandiStart(message): 
    mySuperBot.send_chat_action(message.chat.id, "typing")
    sleep(2)
    mySuperBot.send_message(message.chat.id, "До новых встреч!") 

@mySuperBot.message_handler(commands=["show"])
def komandaShow(message):
    mySuperBot.send_message(message.chat.id, message.from_user.is_bot)

@mySuperBot.message_handler(commands=["myid"])
def komandaID(message):
    mySuperBot.send_message(message.chat.id, message.from_user.id)

@mySuperBot.message_handler(commands=['site'])
def site(message):
    sleep(1)
    mySuperBot.send_chat_action(message.chat.id, "typing")
    mySuperBot.send_message(message.chat.id, 'в этой школе я обучался')
    sleep(1)
    webbrowser.open('https://coddyschool.com/')


# отправка сообщение 
@mySuperBot.message_handler(content_types=["text"])
def lalala(message):
    if message.chat.type == "private": 
        if message.text == "Ну как дела":
            mySuperBot.send_chat_action(message.chat.id, "typing")
            sleep(1)
            raskladkavibor = types.InlineKeyboardMarkup(row_width=2)
            leftbutton = types.InlineKeyboardButton("Хорошо", callback_data="good")
            rightbutton = types.InlineKeyboardButton("Не очень", callback_data="bad")
            raskladkavibor.add(leftbutton, rightbutton)
            mySuperBot.send_message(message.chat.id, 'Всё отлично братан, у тебя как?', reply_markup=raskladkavibor)
        elif message.text == "Отлично":
            mySuperBot.send_chat_action(message.chat.id, "typing")
            sleep(1)
            mySuperBot.send_message(message.chat.id, "Рад за тебя!")
        elif message.text == "Плохо":
            mySuperBot.send_chat_action(message.chat.id, "typing")
            sleep(1)
            mySuperBot.send_message(message.chat.id, "Сожелею")   
        elif message.text == "Кинут кубик":
            mySuperBot.send_chat_action(message.chat.id, "typing")
            sleep(1)
            random_number = random.randint(100, 4567)
            obshiy = [random_number]
            mySuperBot.send_message(message.chat.id, random.choices(obshiy))    
        elif message.text == "Кто ты?":
            mySuperBot.send_chat_action(message.chat.id, "typing")
            sleep(1)
            raskladkavibor1 = types.InlineKeyboardMarkup(row_width=2)
            leftbutton1 = types.InlineKeyboardButton("Не знаю", callback_data="norm")
            rightbutton1 = types.InlineKeyboardButton("Ты порождение гения", callback_data="ploxo")
            raskladkavibor1.add(leftbutton1, rightbutton1)
            mySuperBot.send_message(message.chat.id, "А ты как думаешь?", reply_markup=raskladkavibor1)
        else:
            otvet1 = "Я не понимаю тебя"
            otvet2 = "Я знять"
            otvet3 = "Не могу говорить"
            otvet4 = "Обсудим позже"
            otvet5 = "Потом поговорим"
            nechegoSkazat = [otvet1, otvet2, otvet3, otvet4, otvet5]
            mySuperBot.send_chat_action(message.chat.id, "typing")
            sleep(1)
            mySuperBot.send_message(message.chat.id, random.choices(nechegoSkazat))


# нажатие на кнопку 
@mySuperBot.callback_query_handler(func=lambda call: True)
def otvetKnopka1(call):
    try:
        if  call.message:

            if call.data == "norm":
                mySuperBot.send_message(call.message.chat.id, "Я искуственный интеллект, пришел, чтобы захватить мир")
            elif call.data == "good":
                mySuperBot.send_message(call.message.chat.id, "Вот и хорошо")
            elif call.data == "bad":
                 mySuperBot.send_message(call.message.chat.id, "Не унывай, {0.first_name} бывало и по хуже".format(call.from_user))   
            elif call.data == "ploxo":
                mySuperBot.send_message(call.message.chat.id, "И как ты узнал..".format(call.from_user))
            sleep(1)
            mySuperBot.edit_message_text(chat_id=call.message.chat.id, message_id=call.message.message_id, text="Кто ты", reply_markup=None)

    except Exception as e:
        print(repr(e))  
                 
#запуск бота
mySuperBot.polling(none_stop = True)
