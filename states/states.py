from aiogram.dispatcher.filters.state import StatesGroup, State


class SetText(StatesGroup):
    Text = State()