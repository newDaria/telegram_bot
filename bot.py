#Updater - это компонент отвечающий за коммуникацию с сервером Telegram 
#именно он получает/передает сообщения.
import settings
import logging
from telegram.ext import Updater, CommandHandler,MessageHandler, Filters

logging.basicConfig(filename='bot.log', level=logging.INFO)


# PROXY = {'proxy_url': settings.PROXY_URL,
#     'urllib3_proxy_kwargs': {
#         'username': settings.PROXY_USERNAME, 
#         'password': settings.PROXY_PASSWORD}}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Привет, пользователь! Ты вызвал команду /start')

 #реагировать только на текстовые сообщения
def talk_to_me(update, context):
    user_text = update.message.text 
    print(user_text)
    update.message.reply_text(user_text)

def main():
    # Создаем бота и передаем ему ключ для авторизации на серверах Telegram
    mybot = Updater(settings.API_KEY, use_context=True)
    #mybot.dispatcher для того, чтобы при наступлении события
    dp = mybot.dispatcher
    dp.add_handler(CommandHandler("start", greet_user))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))
    logging.info("Бот стартовал")
    # Командуем боту начать ходить в Telegram за сообщениями
    mybot.start_polling()
    # Запускаем бота, он будет работать, пока мы его не остановим принудительно
    mybot.idle()




# Если вам нужно вызвать функцию не внутри другой функции,
# она заключается в специальный блок, который исполняется только 
# при прямом вызове файла python bot.py и не вызывается при импорте
if __name__ == "__main__":
    main()

