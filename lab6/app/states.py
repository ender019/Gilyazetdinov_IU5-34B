from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import StatesGroup, State
from aiogram.types import Message, ReplyKeyboardRemove

from app.keyboards import Kb

routerr = Router()

class Registration(StatesGroup):
    type = State()
    login = State()
    password = State()


@routerr.message(Command("reg"))
async def reg_start(message: Message, state: FSMContext):
    try: state.clear()
    except: pass
    await state.update_data(user_id=message.from_user.id)
    await message.answer(text="choose root or user:", reply_markup=Kb.type)
    await state.set_state(Registration.type)

@routerr.message(Command("my_data"))
async def output_data(message: Message, state: FSMContext):
    user_data = await state.get_data()
    if len(user_data.keys())==0: await message.answer(text="no data")
    else: await message.answer(text=f"login: {user_data['user_id']}\nlogin: {user_data['type']}\n"
                                    f"login: {user_data['login']}\npassword: {user_data['password']}.")

@routerr.message(F.text, Registration.type)
async def rooting(message: Message, state: FSMContext):
    if message.text not in ["user", "root"]:
        await message.answer(text="error, choose", reply_markup=Kb.type)
        return
    await state.update_data(type=message.text)
    await message.answer(text="Enter login:", reply_markup=ReplyKeyboardRemove())
    await state.set_state(Registration.login)

@routerr.message(F.text, Registration.login)
async def logining(message: Message, state: FSMContext):
    await state.update_data(login=message.text)
    await message.answer(text="Enter password:")
    await state.set_state(Registration.password)

@routerr.message(F.text, Registration.password)
async def passwording(message: Message, state: FSMContext):
    await state.update_data(password=message.text)
    await message.answer(text=f"auntification success")
    await state.set_state(None)