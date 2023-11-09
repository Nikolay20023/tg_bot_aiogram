from aiogram import Router, F
from aiogram.filters import Command
from aiogram.fsm.context import FSMContext
from aiogram.fsm.state import State, StatesGroup
from aiogram.types import Message, ReplyKeyboardRemove

from keyboards.simple_row import make_row_keyboard


router = Router()

available_entity_names = ["Суши", "Пицца", "Плов"]
available_entity_sizes = ["Маленькая", "Средняя", "Большая"]


class OrderFood(StatesGroup):
    choosing_name = State()
    choosing_size = State()


@router.message(Command("food"))
async def cmd_food(message: Message, state: FSMContext):
    await message.answer(
        text="Выберите блюдо",
        reply_markup=make_row_keyboard(available_entity_names)
    )

    await state.set_state(OrderFood.choosing_name)


@router.message(OrderFood.choosing_name, F.text.in_(available_entity_names))
async def food_chosen(message: Message, state: FSMContext):
    await state.update_data(food_chosen=message.text.lower())
    await message.answer(
        text="Спасибо. Теперь выберите размер порции",
        reply_markup=make_row_keyboard(available_entity_sizes)
    )
    await state.set_state(OrderFood.choosing_size)


@router.message(OrderFood.choosing_size, F.text.in_(available_entity_sizes))
async def size_chosen(message: Message, state: FSMContext):
    user_data = await state.get_data()
    await message.answer(
        text=f"Вы выбрали {message.text.lower()} порцию {user_data['food_chosen']}",
        reply_markup=ReplyKeyboardRemove()
    )
    await state.clear()