from telegram.ext.updater import Updater
from telegram.update import Update
from telegram.ext.callbackcontext import CallbackContext
from telegram.ext.commandhandler import CommandHandler
from telegram.ext.messagehandler import MessageHandler
from telegram.ext.filters import Filters
import main as main

updater = Updater("5081044030:AAFBKnCNiMLU3vprBe5vnppEs-wDLaENjqg", use_context=True)


def start(update: Update, context: CallbackContext):
    update.message.reply_text("Engine. Powering. Up.")

def suckmyanus():
    sadge = main.main()
    sadge = ''.join(sadge)
    print(sadge)
    return sadge

def dsb(update: Update, context: CallbackContext):
    update.message.reply_text("On it!")
    while True:
        update.message.reply_text(suckmyanus())
        time.sleep(10)
def help(update: Update, context: CallbackContext):
    update.message.reply_text("I'll post the DSB-Changes in here. Please don't hurt me.")

def source(update: Update, context: CallbackContext):
    update.message.reply_text("https://github.com/Maihoernchen/dsbapibutonly4me")

def unknown_text(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry I can't recognize you , you said '%s'" % update.message.text)

def unknown(update: Update, context: CallbackContext):
    update.message.reply_text(
        "Sorry '%s' is not a valid command" % update.message.text)


updater.dispatcher.add_handler(CommandHandler('start', start))
updater.dispatcher.add_handler(CommandHandler('dsb', dsb))
updater.dispatcher.add_handler(CommandHandler('help', help))
updater.dispatcher.add_handler(CommandHandler('source', source))
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown))
updater.dispatcher.add_handler(MessageHandler(
    # Filters out unknown commands
    Filters.command, unknown))

# Filters out unknown messages.
updater.dispatcher.add_handler(MessageHandler(Filters.text, unknown_text))

updater.start_polling()