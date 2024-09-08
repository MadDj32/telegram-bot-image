from telegram import Update
from telegram.ext import Application, CommandHandler, CallbackContext

# Замените 'ваш_токен' на действительный токен
TOKEN = '7225397168:AAHwFOFmbptPq9jHbHl3VzJhdwFv86IZPig'

# Путь к вашему изображению
IMAGE_PATH = 'C:/Users/Bot/111.png'

async def start(update: Update, context: CallbackContext) -> None:
    # Отправляем изображение
    await update.message.reply_photo(photo=open(IMAGE_PATH, 'rb'))

def main():
    application = Application.builder().token(TOKEN).build()

    application.add_handler(CommandHandler("start", start))

    application.run_polling()

if __name__ == '__main__':
    main()