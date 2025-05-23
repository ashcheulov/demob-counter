import asyncio
from aiogram import Bot, Dispatcher, F
from aiogram.enums import ParseMode
from aiogram.types import (
    Message,
    ReplyKeyboardMarkup,
    KeyboardButton,
    WebAppInfo,
    InlineKeyboardMarkup,
    InlineKeyboardButton,
)
from aiogram.client.default import DefaultBotProperties

# 🔒 Токен от BotFather
BOT_TOKEN = "7380534180:AAEBP2VcY363wUpiibe_k7MfPZtKxsEVTKE"

# 🌐 URL WebApp
WEBAPP_URL = "https://demob-counter.vercel.app"

# ✅ Настройка бота
bot = Bot(
    token=BOT_TOKEN,
    default=DefaultBotProperties(parse_mode=ParseMode.HTML)
)

dp = Dispatcher()

# 🔁 Обработчик команды /start
@dp.message(F.text.startswith("/start"))
async def start_handler(message: Message):
    if message.chat.type == "private":
        # 📲 В личке — кнопка с WebApp
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
        # 👥 В группе — инлайн-кнопка со ссылкой на бота
        bot_username = (await bot.get_me()).username
        keyboard = InlineKeyboardMarkup(
            inline_keyboard=[
                [
                    InlineKeyboardButton(
                        text="Открыть счётчик дембеля (в личке)",
                        url=f"https://t.me/demobilzationbot"
                    )
                ]
            ]
        )
        await message.answer(
            "📌 Счётчик можно открыть только в личных сообщениях.\nНажми кнопку ниже, чтобы перейти:",
            reply_markup=keyboard
        )

# 💬 Логируем любые сообщения (можно удалить)
@dp.message()
async def catch_all(message: Message):
    print(f"[{message.chat.type}] {message.from_user.username}: {message.text}")

# 🚀 Запуск бота
async def main():
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
