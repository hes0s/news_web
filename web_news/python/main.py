import aiogram
from aiogram import Dispatcher, Bot
import asyncio
from aiogram.filters import CommandStart
from aiogram.types import Message
import logging

import kbs as kb

bot = Bot("7910281070:AAGWK1H3xMzxtVsrHH6t_BM_wDe7Ls4KR4o")
dp = Dispatcher()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello, look down", reply_markup=kb.adr)

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())



# In planuri  e de adaugat FMS si keyboard, si de introdus baza de date 
