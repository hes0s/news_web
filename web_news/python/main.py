import aiogram
from aiogram import F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import ContentType
from aiogram import Dispatcher, Bot
import asyncio
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, PhotoSize
import logging
from db import conn, cursor

import kbs as kb

bot = Bot("7910281070:AAGWK1H3xMzxtVsrHH6t_BM_wDe7Ls4KR4o")
dp = Dispatcher()

# FSM States
class Form_FMS(StatesGroup):
    name = State()
    description = State()
    photo = State()

@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello, look down", reply_markup=kb.adr)

# Start FSM Process
@dp.message(Command(commands=["Add"]))
async def add(message: Message, state: FSMContext):
    await state.set_state(Form_FMS.name)
    await message.answer("Enter name")

# Process Name
@dp.message(Form_FMS.name)
async def proces_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)  # Save Name
    await state.set_state(Form_FMS.description)
    await message.answer("Enter description")

# Process Description
@dp.message(Form_FMS.description)
async def process_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)  # Save Description
    await state.set_state(Form_FMS.photo)
    await message.answer("Send a photo")

# Process Photo
@dp.message(Form_FMS.photo, F.content_type == types.ContentType.PHOTO)
async def process_photo(message: Message, state: FSMContext):
    data = await state.get_data()  

    name = data.get("name")
    description = data.get("description")
    file_id = message.photo[-1].file_id  

    
    file = await bot.get_file(file_id)
    file_path = file.file_path
    photo = await bot.download_file(file_path)

    
    cursor.execute("INSERT INTO news_info (Name, Description, img_url) VALUES (%s, %s, %s)",
                   (name, description, file_id))
    conn.commit()

    await message.answer("News added successfully! ✅")
    await state.clear()

async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())