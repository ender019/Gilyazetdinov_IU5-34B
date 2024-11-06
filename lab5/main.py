import asyncio
from aiogram import Bot, Dispatcher

from app.handlers import router

async def main():
    TOKEN = "1363922324:AAGO8DJjaUD3RsR9MjWA5V1UENlMYvzhttM"
    bot = Bot(token=TOKEN)
    dp = Dispatcher()
    dp.include_router(router)
    await dp.start_polling(bot)

if __name__ == "__main__":
    try: asyncio.run(main())
    except KeyboardInterrupt: print("end")