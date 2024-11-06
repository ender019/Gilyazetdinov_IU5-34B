from aiogram import html, F, Router
from aiogram.types import ReplyKeyboardMarkup, KeyboardButton, InlineKeyboardMarkup, InlineKeyboardButton

class Kb:
    main = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="1")],
                                         [KeyboardButton(text="2")],
                                         [KeyboardButton(text="3"), KeyboardButton(text="4")]],
                               resize_keyboard=True, input_field_placeholder="choose...")

    ctlg = InlineKeyboardMarkup(inline_keyboard=[[InlineKeyboardButton(text="9", callback_data="ib9")],
                                                 [InlineKeyboardButton(text="8", callback_data="ib8")],
                                                 [InlineKeyboardButton(text="7", callback_data="ib7")]])

    type = ReplyKeyboardMarkup(keyboard=[[KeyboardButton(text="user"), KeyboardButton(text="root")]],
                               resize_keyboard=True, input_field_placeholder="choose role")