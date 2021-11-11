from datetime import datetime, timedelta

from telebot import types

from python.project.db import DataBase
from python.project.utils import bot


def notify_info(id_user):
    keyboard = types.InlineKeyboardMarkup()
    new_notify = types.InlineKeyboardButton(text='Создать напоминание', callback_data='create_notify')
    keyboard.add(new_notify)
    show_notify = types.InlineKeyboardButton(text='Показать напоминания', callback_data='show_notify')
    keyboard.add(show_notify)
    question = 'Что сделать?'
    bot.send_message(id_user, text=question, reply_markup=keyboard)


def create_notify(message):
    notify = {
        "name": message.text
    }
    bot.send_message(message.from_user.id, text='Введите дату дд-мм-гггг чч:мм')
    bot.register_next_step_handler(message, fill_notify_date, notify)


def fill_notify_date(message, notify):
    date = datetime.strptime(message.text, '%d-%m-%Y %H:%M')
    notify["date"] = date
    bot.send_message(message.from_user.id, text='За сколько дней напомнить?')
    bot.register_next_step_handler(message, fill_notify_delay, notify)


def fill_notify_delay(message, notify):
    id_user = message.from_user.id
    notify["delay"] = int(message.text)
    notify["id_user"] = id_user

    db = DataBase().get_connection()
    collection = db["notify"]
    collection.insert_one(notify)

    bot.send_message(message.from_user.id, text='Напоминание созданно')
    notify_info(id_user)


def show_notifies(call):
    text = "Ваши напоминая\n"
    id_user = call.from_user.id

    db = DataBase().get_connection()
    collection = db["notify"]
    results = collection.find({"id_user": id_user})
    for elem in results:
        text += print_notify(elem)
    bot.send_message(call.from_user.id, text=text)


def check_notifies():
    db = DataBase().get_connection()
    collection = db["notify"]
    results = collection.find()
    now = datetime.now()
    for elem in results:
        if now >= elem["date"] or now >= elem["date"] - timedelta(elem["delay"]):
            bot.send_message(elem["id_user"], text=print_notify(elem))


def print_notify(notify):
    text = "Название: " + notify["name"] + " "
    text += "Дата: " + str(notify["date"]) + " "
    text += "Напомнить за : " + str(notify["delay"]) + " дня\n"
    return text
