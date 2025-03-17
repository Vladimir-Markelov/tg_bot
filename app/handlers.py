from aiogram import F, Router
from aiogram.types import Message
from aiogram.filters import CommandStart
from aiogram.fsm.state import State, StatesGroup
from aiogram.fsm.context import FSMContext
from app.generate import ai_generate

route = Router()

class Gen(StatesGroup):
    wait = State()

@route.message(CommandStart())
async def cmd_start(message: Message):
    await message.answer('Hi, write your question!')

@route.message(Gen.wait)
async def stop_rep(message: Message):
    await message.answer('Please, wait...')

@route.message()
async def generation(message: Message, state: FSMContext):
    await state.set_state(Gen.wait)
    response = await ai_generate(message.text)
    await message.answer(response, parse_mode='Markdown')
    await state.clear()