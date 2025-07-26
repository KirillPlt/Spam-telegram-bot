"""
    Created by @code_its_me
    License: MIT
"""


from pyrogram import Client, filters
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton


WORDS: list = ['пиар', 'piar', 'подписки', 'chat', 'чат', 'чаты']

api_id = ''  # Ваш api_id.
api_hash = ''  # Ваш api_hash.
phone_number = ''  # Ваш номер телефона.
username = ''  # Ваш username.
text = ''  # Ваше спам-сообщение.

app = Client("spam_bot", api_id=api_id, api_hash=api_hash, phone_number=phone_number)


@app.on_message(filters.command("piar") & filters.user(username) & filters.private)
def start_piar(client, message):
    app.send_message(username, 'Спам начался!')

    # Получаем диалоги
    chats = app.get_dialogs()

    for chat in chats:
        if chat.chat.type in [ChatType.SUPERGROUP, ChatType.GROUP]:
            chat_title = chat.chat.title

            for word in WORDS:
                if chat_title and word in chat_title.lower():
                    try:
                        app.send_message(
                            chat_id=chat.chat.id,
                            text=text,
                            reply_markup=keyboard
                        )
                    except Exception as e:
                        print(f'Ошибка в {chat_title}({chat.chat.id}): {e}')

    message.reply('Спам отправлен!')

app.run()
