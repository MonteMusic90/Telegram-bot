
import logging

from telegram.ext import Updater, CommandHandler, MessageHandler, Filters

# Enable logging
logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
                    level=logging.INFO)

logger = logging.getLogger(__name__)


#Command Handlers
def start(update, context):
    update.message.reply_text('I AM ALIVE!')


#function to respond to help cmd
def help(update, context):
    update.message.reply_text('I am currently not smart enough to help you.')

def anime(update,context):
    update.message.reply_text('Death Note is a good introduction into Anime!') 

def vixen(update,context):
    update.message.reply_text('Who other than Melyssa Ford...Really?') 

def drink(update,context):
    update.message.reply_text('I recommend Jameson.')              

#function to echo the users message
def echo(update, context):
    update.message.reply_text(update.message.text + '' + ' AND JOSH IS THE GREATEST.')
   

#function to log errors and display
def error(update, context):
    logger.warning('Update "%s" caused error "%s"', update, context.error)


def main():
    updater = Updater("5398352720:AAEeZuwrMNtpQBylhsYyLEXTN9AIXN2TXG0", use_context=True)
   

    dp = updater.dispatcher

    dp.add_handler(CommandHandler("start", start))
    dp.add_handler(CommandHandler("help", help))
    dp.add_handler(CommandHandler("anime", anime))
    dp.add_handler(CommandHandler("vixen", vixen))
    dp.add_handler(CommandHandler("drink", drink))
    
    dp.add_handler(MessageHandler(Filters.text, echo))

    dp.add_error_handler(error)

    updater.start_polling()

    updater.idle()


if __name__ == '__main__':
    main()