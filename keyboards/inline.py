from aiogram.types import InlineKeyboardMarkup, InlineKeyboardButton

start_kb = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text='Да', callback_data='da'),
            InlineKeyboardButton(text='Нет', callback_data='no')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True  
)

da_kb = InlineKeyboardMarkup(
    inline_keyboard= [
        [
            InlineKeyboardButton(text='Фото', callback_data='foto'),
            InlineKeyboardButton(text='Видео', callback_data='video'),
        ],
        [
            InlineKeyboardButton(text='Текст', callback_data='text'),
            InlineKeyboardButton(text='Аудио', callback_data='audio')
        ],
        [
            InlineKeyboardButton(text='Документ', callback_data='document')
        ]
    ],
    resize_keyboard=True,
    one_time_keyboard=True
)