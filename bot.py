import os
from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Получаем токен из переменных среды
TOKEN = os.getenv('TOKEN')

# Путь к вашему изображению относительно корня проекта
IMAGE_PATH = '111.png'

async def start(update: Update, context: CallbackContext) -> None:
    # Отправляем изображение
    with open(IMAGE_PATH, 'rb') as photo:
        await update.message.reply_photo(photo=photo)

def main():
    # Создаем объект приложения с токеном из переменных среды
    application = Application.builder().token(TOKEN).build()

    # Добавляем обработчик команды /start
    application.add_handler(CommandHandler("start", start))

    # Запускаем бота
    application.run_polling()

if __name__ == '__main__':
    main()
