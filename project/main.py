import threading

from telebot import types

from python.project import notify, wolframalpha_api
from python.project.utils import bot


@bot.message_handler(content_types=['text'])
def start(message):
    keyboard = types.InlineKeyboardMarkup()
    key_notify = types.InlineKeyboardButton(text='Напоминалка', callback_data='notify')
    keyboard.add(key_notify)
    wolfram_alpha = types.InlineKeyboardButton(text='wolfram alpha', callback_data='wolfram')
    keyboard.add(wolfram_alpha)
    question = 'Какой функционал'
    bot.send_message(message.from_user.id, text=question, reply_markup=keyboard)


@bot.callback_query_handler(func=lambda call: True)
def callback_worker(call):
    if call.data == "notify":
        notify.notify_info(call.from_user.id)
    elif call.data == "create_notify":
        bot.send_message(call.from_user.id, text='Введите название')
        bot.register_next_step_handler(call.message, notify.create_notify)
    elif call.data == "show_notify":
        notify.show_notifies(call)
    elif call.data == 'wolfram':
        bot.send_message(call.from_user.id, text='Введите, что нужно решить(синтаксис Wolfram Alpha)')
        bot.register_next_step_handler(call.message, wolframalpha_api.solve)


if __name__ == '__main__':
    notify_thread = threading.Thread(target=notify.check_notifies)
    notify_thread.start()
    bot.polling()
