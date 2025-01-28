import aiogram
from aiogram import Dispatcher, Bot
import asyncio

bot = Bot("7910281070:AAGWK1H3xMzxtVsrHH6t_BM_wDe7Ls4KR4o")
dp = Dispatcher()


async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    asyncio.run(main())