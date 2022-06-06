import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters, CallbackContext
from telegram import Update, Bot


token = "5583136037:AAGzj1ANZ4Qr6_xSyofkQ6pxPfhWNsmqmoM"


def echo_text(bot, update):
    reply = update.message.text
    bot.send_message(chat_id=update.message.chat_id, text=reply)


def greeting(update: Update, context: CallbackContext):
     update.message.reply_text("Alan sosi pisos Alan sosi pisos")



def message_handler(update: Update, context: CallbackContext):
    text = update.to_dict()['message']['text']
    update.message.reply_text(text)


def main():
    updater = Updater(token)
    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", greeting))
    dp.add_handler(MessageHandler(Filters.text, message_handler))

    updater.start_polling()
    updater.idle()

if __name__ == "__main__":
    main()
