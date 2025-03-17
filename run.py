import asyncio
from aiogram import Bot, Dispatcher
from config import TG_TOKEN
from app.handlers import route

async def main():
    bot = Bot(token=TG_TOKEN)
    dp = Dispatcher()
    dp.include_router(route)
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())