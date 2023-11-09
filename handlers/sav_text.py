from typing import Optional
from aiogram import Router, F
from aiogram.types import Message
from aiogram.filters import Command, CommandObject
from aiogram.fsm.context import FSMContext

from states import SaveCommon
from states import TextSave
from filters.text_has_link import HasLinkFilter
from storage import add_link


router = Router()


@router.message(SaveCommon.waiting_for_save_start, F.text, HasLinkFilter())
async def text_save_link(message: Message, link: str, state: FSMContext):
    await state.update_data(link=link)
    await state.set_state(TextSave.waiting_for_title)
    await message.answer(
        text=f"Окей, я нашёл ссылку в сообщение {link}. "
             f"Теперь отправь мне описания (не больше 30 символов)"
    )


@router.message(SaveCommon.waiting_for_save_start, F.text)
async def save_text_no_link(message: Message):
    await message.answer(
        text="Эм.. я не нашёл в твоём сообщении ссылку. "
             "Попробую ещё раз или нажми /cancel, чтобы отменить действия " 
    )


@router.message(TextSave.waiting_for_title, F.text.func(len) <= 30)
async def title_entered_ok(message: Message, state: FSMContext):
    await state.update_data(title=message.text, description=None)
    await state.set_state(TextSave.waiting_for_description)
    await message.answer(
        text="Заголовок вижу.Введите описания"
            "(Не больше 30 символов)"
            "или нажми /skip, чтобы пропустить этот шаг"
    )


@router.message(TextSave.waiting_for_description, F.text.func(len) <= 30)
@router.message(TextSave.waiting_for_description, Command("skip"))
async def last_step(
    message: Message,
    state: FSMContext,
    command: Optional[CommandObject] = None
):
    if not command:
        await state.update_data(description=message.text)
    
    data = await state.get_data()
    add_link(message.from_user.id, data["link"], data["title"], data["description"])

    await message.answer("Ссылка сохранена")
    await state.clear()


@router.message(TextSave.waiting_for_title, F.text)
@router.message(TextSave.waiting_for_title, F.text)
async def text_long_title(message: Message):
    await message.answer("Слишком длинный заголовок. Попробуй ещё раз")
    return 

