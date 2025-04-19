import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
)
from aiogram.client.default import DefaultBotProperties

# 🔒 Токен от BotFather
BOT_TOKEN = "7380534180:AAEBP2VcY363wUpiibe_k7MfPZtKxsEVTKE"

# 🌐 URL WebApp
WEBAPP_URL = "https://demob-counter.vercel.app"

# ✅ Указываем parse_mode по-новому
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

# Обработчик команды /start для личных сообщений
@dp.message(F.text == "/start")
async def start_handler(message: Message):
    keyboard = ReplyKeyboardMarkup(
        resize_keyboard=True,
        keyboard=[
            [
                KeyboardButton(
                    text="Открыть счётчик дембеля",
                    web_app=WebAppInfo(url=WEBAPP_URL)
                )
            ]
        ]
    )
    await message.answer("Нажми кнопку ниже, чтобы открыть счётчик ⏳", reply_markup=keyboard)

# Обработчик для сообщения с ссылкой на WebApp в группе
@dp.message(F.text == "Открыть счётчик дембеля")
async def send_webapp_link(message: Message):
    await message.answer(
        "Нажми на ссылку ниже, чтобы открыть счётчик дембеля:",
        reply_markup=ReplyKeyboardMarkup(
            resize_keyboard=True,
            keyboard=[
                [KeyboardButton(text="Открыть WebApp", url=WEBAPP_URL)]
            ]
        )
    )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
