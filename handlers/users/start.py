from asyncio import sleep

from aiogram import types
from aiogram.dispatcher import FSMContext

from loader import dp, bot
from states.states import SetText
from utils.db_api.db import DBComm


@dp.message_handler(commands='settext', state='*')
async def set_text(message: types.Message):
    await message.answer('Введите текст')
    await SetText.Text.set()


@dp.message_handler(state=SetText.Text)
async def edit_text(message: types.Message, state: FSMContext):
    text = message.text
    await DBComm.db_edit_text(text)
    await message.answer('Успешно')
    await state.reset_state()


@dp.message_handler(commands='settime', state='*')
async def set_time(message: types.Message, state: FSMContext):
    async with state.proxy() as data:
        data['time'] = message.get_args()
        time = int(data['time'])
    await DBComm.db_edit_time(time)
    await message.answer(f'Текущее время до удаления - {time}')


@dp.message_handler(text="g", state='*')
async def on_user_join(message: types.Message, state: FSMContext):
    m_id = await message.answer(await DBComm.db_get_text())
    m_id = m_id['message_id']
    time = int(await DBComm.db_get_time())
    await sleep(time)
    await bot.delete_message(chat_id=message.chat.id, message_id=m_id)
