import logging
import enhance_quality
from aiogram import Bot, Dispatcher, executor

API_TOKEN = "5856647351:AAFOwmzTK5JLamZAGs1gEkwAEQrj1Ry8XKg"

# Configure logging
logging.basicConfig(level=logging.INFO)

# Initialize bot and dispatcher
bot = Bot(token=API_TOKEN)
dp = Dispatcher(bot)


@dp.message_handler(commands=['start', 'help'])
async def send_welcome(message):
    """
    This handler will be called when user sends `/start` or `/help` command
    """
    await bot.send_message(chat_id=message.chat.id, text="Hi There😄️!")
    await bot.send_photo(chat_id=message.chat.id, photo=open('Textures/de_niro.png', 'rb'))
    await bot.send_message(chat_id=message.chat.id, text="\n\n\nSend me a picture you want to enhance the quality of.\nI will increase it by 4 times and send it back to you😎️")


@dp.message_handler(content_types=['photo', 'document'])
async def doc_handler(message):
    if document := message.document:
        await document.download(
            # destination_dir="your/folder/",
            destination_file="test",
        )
        print('downloaded')

    
    enhance_quality.enhance()

    # os.remove('test.jpg')
    result: message = await bot.send_document(chat_id=message.chat.id, document=open('your_pic_enhanced.jpg', 'rb'))


if __name__ == '__main__':
    executor.start_polling(dp, skip_updates=True)
