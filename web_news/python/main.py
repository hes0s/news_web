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

import kbs as kb

bot = Bot("7910281070:AAGWK1H3xMzxtVsrHH6t_BM_wDe7Ls4KR4o")
dp = Dispatcher()


#               FMS States 
class Form_FMS(StatesGroup):
    name = State()
    description = State()
    photo = State()


@dp.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer("Hello, look down", reply_markup=kb.adr)

#           FMS Machine 

#Enter in FMS machine
@dp.message(Command(commands=["Add"]))
async def add(message: Message, state: FSMContext )-> None:
    await state.set_state(Form_FMS.name)
    await message.answer("Enter name")

@dp.message(Form_FMS.name)
async def proces_name(message: Message, state: FSMContext)-> None:
    await state.update_data(name=message.text)  # Saving FMS name 
    await state.set_state(Form_FMS.description)
    await message.answer("Enter description")
    # Setting next step FMS description

# Saving FMS description
@dp.message(Form_FMS.description)
async def process_description(message: Message, state: FSMContext)-> None:
    await state.update_data(description=message.text) 
    await state.set_state(Form_FMS.photo)
    await message.answer("Enter photo")
    # Setting next step FMS photo

@dp.message(Form_FMS.photo, F.content_type == types.ContentType.PHOTO)
async def process_photo(message: Message, state: FSMContext)-> None:
    await state.update_data(photo=message.photo[-1].file_id)
    data = await state.get_data()
    await message.answer(f"Name: {data['name']}\nDescription: {data['description']}\nPhoto: {data['photo']}")
    await state.clear()




async def main():
    await dp.start_polling(bot)

if __name__ == '__main__':
    logging.basicConfig(level=logging.INFO)
    asyncio.run(main())



# In planuri  e de adaugat FMS si keyboard, si de introdus baza de date 


