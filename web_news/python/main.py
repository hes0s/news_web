import os
import logging
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from dotenv import load_dotenv
from db import conn, cursor  # Import database connection

# Load environment variables
load_dotenv()

# Bot & Dispatcher
BOT_TOKEN = os.getenv("BOT_TOKEN")
bot = Bot(BOT_TOKEN)
dp = Dispatcher()

# FSM States
class FormFSM(StatesGroup):
    name = State()
    description = State()
    photo = State()

# Command: Start
@dp.message(F.text == "/start")
async def cmd_start(message: Message):
    await message.answer("Hello! Use /add to enter adding mode.")

# Start FSM Process
@dp.message(F.text == "/add")
async def add(message: Message, state: FSMContext):
    await message.answer("You entered adding mode. Please follow the instructions.")
    await state.set_state(FormFSM.name)
    await message.answer("Enter name:")

# Process Name
@dp.message(FormFSM.name)
async def process_name(message: Message, state: FSMContext):
    await state.update_data(name=message.text)
    await state.set_state(FormFSM.description)
    await message.answer("Enter description:")

# Process Description
@dp.message(FormFSM.description)
async def process_description(message: Message, state: FSMContext):
    await state.update_data(description=message.text)
    await state.set_state(FormFSM.photo)
    await message.answer("Send a photo:")

# Process Photo
@dp.message(FormFSM.photo, F.content_type == types.ContentType.PHOTO)
async def process_photo(message: Message, state: FSMContext):
    data = await state.get_data()

    name = data.get("name")
    description = data.get("description")
    file_id = message.photo[-1].file_id  

    # Save to SQLite
    cursor.execute(
        "INSERT INTO news ( newsName, newsDesription, IMG_URL) VALUES (?, ?, ?)",
        ( name, description, file_id),
    )
    conn.commit()

    await message.answer("News added successfully!")
    await state.clear()

# Run the bot
async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())