from aiogram import Router, F
from aiogram.filters import CommandStart, Command
from aiogram.types import Message, CallbackQuery, ContentType

from keyboards.inline import start_kb, da_kb
from lexicon.lexicon import LEXICON


router = Router()

@router.message(CommandStart())
async def start(message: Message):
    await message.answer(f'Привет, {message.from_user.first_name}, хочешь продолжить?', reply_markup=start_kb)


@router.callback_query(F.data == 'da')
async def otvda(callback: CallbackQuery):
    await callback.message.edit_text(text='<tg-spoiler>Что вам отправить?</tg-spoiler>', reply_markup=da_kb)


@router.callback_query(F.data.in_(['foto', 'video', 'document', 'audio', 'text']))
async def oops(callback: CallbackQuery):
    await callback.answer(text='Отправьте лучше сами, я сломался :_)', show_alert=True)

#TODO: Обрабатываю каждый тип отдельно
@router.message(F.content_type == ContentType.DOCUMENT)
async def other(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
        await message.answer(f'Вот айди вашего документа {message.document.file_id}')
    except TypeError:
        await message.reply(f'НЕ поддерживается методом send_copy')

@router.message(F.content_type == ContentType.PHOTO)
async def other(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
        await message.answer(f'Вот айди вашего фото {message.photo[-1].file_id}')
    except TypeError:
        await message.reply(f'НЕ поддерживается методом send_copy')


@router.message(F.content_type == ContentType.VIDEO)
async def other(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
        await message.answer(f'Вот айди вашего видео {message.video.file_id}')
    except TypeError:
        await message.reply(f'НЕ поддерживается методом send_copy')

@router.message(F.content_type == ContentType.AUDIO)
async def other(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
        await message.answer(f'Вот айди вашего аудио {message.audio.file_id}')
    except TypeError:
        await message.reply(f'НЕ поддерживается методом send_copy')
    


@router.message(F.content_type == ContentType.VOICE)
async def other(message: Message):
    try:
        await message.send_copy(chat_id=message.chat.id)
        await message.answer(f'Вот айди вашего голосового сообщения {message.voice.file_id}')
    except TypeError:
        await message.reply(f'НЕ поддерживается методом send_copy')