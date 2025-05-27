
from aiogram import F, Router, types
from aiogram.filters.command import CommandStart
from aiogram.fsm.state import StatesGroup, State
from aiogram.fsm.context import FSMContext
from src.telegram_core.test_db import token_git, user
from src.gitlab_core.core import test
start_route = Router()

class StartState(StatesGroup):
    token = State()
@start_route.message(CommandStart())
async def cmd_start(message: types.Message, state: FSMContext):
    test()
    await message.answer("Кидай токен")
    await state.set_state(StartState.token)

    
@start_route.message(StartState.token, F.text)
async def get_token(message: types.Message, state: FSMContext):
    await message.answer("Токен получен")
    token_git = message.text
    user = message.from_user.full_name
    await state.clear()
    