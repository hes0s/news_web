from aiogram.types import ReplyKeyboardMarkup, KeyboardButton

main = ReplyKeyboardMarkup(keyboard=[   # main keyboard 
    [KeyboardButton(text='Start')]
])

adr = ReplyKeyboardMarkup(keyboard=[
    [KeyboardButton(text='Rewiew'), KeyboardButton(text='Add')],
    [KeyboardButton(text='Return to main page')]
])