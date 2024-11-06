from aiogram import html, F, Router
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import default_state
from aiogram.filters import CommandStart, Command, StateFilter
from aiogram.types import Message, CallbackQuery

from app.keyboards import Kb

router = Router()

@router.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer(f"Hello, {html.bold(message.from_user.full_name)}!", reply_markup=Kb.main)

@router.message(Command("help"))
async def cmd_help(message: Message):
    await message.reply("команды:\n/help\n/start\n/covid\n/smile")

@router.message(StateFilter(None), Command(commands=["cancel"]))
@router.message(default_state, F.text.lower() == "отмена")
async def cmd_cancel_no_state(message: Message, state: FSMContext):
    await state.set_data({})
    await message.answer(text="Нечего отменять")

@router.message(Command(commands=["cancel"]))
@router.message(F.text.lower() == "отмена")
async def cmd_cancel(message: Message, state: FSMContext):
    await state.clear()
    await message.answer(text="Действие отменено")

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
    try: await message.send_copy(chat_id=message.chat.id)
    except TypeError: await message.answer("Nice try!")