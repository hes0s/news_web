import os
import logging
import time
import asyncio
from aiogram import Bot, Dispatcher, F, types
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message
from dotenv import load_dotenv
from db import conn, cursor  # Import database connection
from PIL import Image
import re
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

@dp.message(FormFSM.photo, F.content_type == types.ContentType.PHOTO)
async def process_photo(message: Message, state: FSMContext):
    
    data = await state.get_data()
    name = data.get("name")
    description = data.get("description")
    file_id = message.photo[-1].file_id  

    # Create directory if it doesn't exist
    directory = './web_news/python/photos'
    if not os.path.exists(directory):
        os.mkdir(directory)
        print("Directory created:", directory)
        

    # Get file information from Telegram
    file_info = await bot.get_file(file_id)
    remote_file_path = file_info.file_path
    
    existing_files = [f for f in os.listdir(directory) if re.match(r'photo_(\d)+.jpg', f)]
    existing_numbers = [int(re.findall(r'\d+', f)[0]) for f in existing_files]
    i = max(existing_numbers) + 1 if existing_numbers else 1
    # Generate a new file name
    new_filename = f"photo_{i}.jpg"
    local_file_path = os.path.join(directory, new_filename)

    # Download the file from Telegram and save it locally using the new file name
    await bot.download_file(remote_file_path, local_file_path)

    # Save the record in the database, storing the local file path
    cursor.execute(
         "INSERT INTO news (newsName, newsDesription, IMG_URL) VALUES (?, ?, ?)",
        (name, description, remote_file_path),
    )
    conn.commit()

    await message.answer("News added successfully!")
    await state.clear()

async def main():
    logging.basicConfig(level=logging.INFO)
    await dp.start_polling(bot)

if __name__ == "__main__":
    asyncio.run(main())
