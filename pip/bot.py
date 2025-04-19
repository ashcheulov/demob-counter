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

# 🔁 Универсальный обработчик /start
@dp.message(F.text == "/start")
async def start_handler(message: Message):
    if message.chat.type == "private":
        # 💬 Личка → кнопка с WebApp
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
        await message.answer(
            "Нажми кнопку ниже, чтобы открыть счётчик ⏳",
            reply_markup=keyboard
        )
    else:
        # 👥 Группа → кнопка со ссылкой в ЛС
        bot_username = (await bot.get_me()).username
        keyboard = ReplyKeyboardMarkup(
            resize_keyboard=True,
            keyboard=[
                [
                    KeyboardButton(
                        text="Открыть счётчик дембеля (в личке)",
                        url=f"https://t.me/{bot_username}"
                    )
                ]
            ]
        )
        await message.answer(
            "📌 WebApp можно открыть только в личных сообщениях.\nНажми кнопку ниже, чтобы перейти:",
            reply_markup=keyboard
        )

async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
