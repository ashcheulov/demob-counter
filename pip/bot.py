from aiogram import Bot, Dispatcher, types
from aiogram.types import WebAppInfo, ReplyKeyboardMarkup, KeyboardButton
from aiogram.utils import executor

# 🔒 ВСТАВЬ СЮДА СВОЙ ТОКЕН от BotFather
BOT_TOKEN = "7380534180:AAEBP2VcY363wUpiibe_k7MfPZtKxsEVTKE"

# 🌐 ВСТАВЬ СЮДА ССЫЛКУ НА СВОЙ WEBAPP
WEBAPP_URL = "https://demob-counter.vercel.app/"

bot = Bot(token=BOT_TOKEN)
dp = Dispatcher(bot)

@dp.message_handler(commands=['start'])
async def start(message: types.Message):
    keyboard = ReplyKeyboardMarkup(resize_keyboard=True)
    keyboard.add(KeyboardButton(
        text="Открыть счётчик дембеля",
        web_app=WebAppInfo(url=WEBAPP_URL)
    ))
    await message.answer("Нажми кнопку ниже, чтобы открыть счётчик ⏳", reply_markup=keyboard)

if __name__ == '__main__':
    executor.start_polling(dp)
