from aiogram import html, F, Router
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery

from app.keyboards import Kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=Kb.main)

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.reply("команды:\n/help\n/start\n/covid\n/smile")

@router.message(F.text == "ggg")
async def msg_catch(message: Message):
    await message.answer("fff")

@router.message(F.text == "1")
async def rkb_one(message: Message):
    await message.answer("Choose", reply_markup=Kb.ctlg)

@router.callback_query(F.data == "ib9")
async def ikb_nine(callback: CallbackQuery):
    await callback.answer("accept")
    await callback.message.answer("its 9")

@router.message()
async def echo_handler(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
    except TypeError:
        await message.answer("Nice try!")