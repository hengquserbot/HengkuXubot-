from pykeyboard import InlineKeyboard
from pyrogram.errors import MessageNotModified
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InputTextMessageContent)

from PyroUbot import *


class Button:
    def alive(get_id):
        button = [
            [
                InlineKeyboardButton(
                    text="Tutup",
                    callback_data=f"alv_cls {int(get_id[1])} {int(get_id[2])}",
                )
            ]
        ]
        return button

    def button_add_expired(user_id):
        buttons = InlineKeyboard(row_width=3)
        keyboard = []
        for X in range(1, 13):
            keyboard.append(
                InlineKeyboardButton(
                    f"{X} ʙᴜʟᴀɴ",
                    callback_data=f"success {user_id} {X}",
                )
            )
        buttons.add(*keyboard)
        buttons.row(InlineKeyboardButton("👤 Dapatkan Profil 👤", callback_data=f"profil {user_id}"))
        buttons.row(InlineKeyboardButton("❌ Tolak Pembayaran ❌", callback_data=f"failed {user_id}"))
        return buttons

    def expired_button_bot():
        button = [
            [
                InlineKeyboardButton(
                    text=f"{bot.me.first_name}",
                    url=f"https://t.me/{bot.me.username}",
                )
            ]
        ]
        return button

    def start(message):
        if not message.from_user.id == OWNER_ID:
            button = [
                [InlineKeyboardButton("Beli Userbot", callback_data="bahan")],
                [
                 InlineKeyboardButton("Status Akun", callback_data="status_ubot"),
                 InlineKeyboardButton("Tutor Deploy", url=f"https://t.me/DevsOfNeko/5"),
                ],
                [
                    InlineKeyboardButton("Modul Help", callback_data="help_back"),
                    InlineKeyboardButton("Live Chat", callback_data="support"),
                ],
            ]
        else:
            button = [
                [InlineKeyboardButton("Buat Userbot", callback_data="bahan")],
                [
                    InlineKeyboardButton("Update", callback_data="gitpull"),
                    InlineKeyboardButton("Restart", callback_data="restart"),
                ],
                [
                    InlineKeyboardButton("Pemake Userbot", callback_data="cek_ubot"),
                    InlineKeyboardButton("Modul Help", callback_data="help_back"),
                ],
            ]
        return button

    def plus_minus(query, user_id):
        button = [
            [
                InlineKeyboardButton(
                    "-1 Bulan",
                    callback_data=f"kurang {query}",
                ),
                InlineKeyboardButton(
                    "+1 Bulan",
                    callback_data=f"tambah {query}",
                ),
            ],
            [InlineKeyboardButton("✅️ Konfirmasi", callback_data="confirm")],
            [InlineKeyboardButton("❌ Batalkan", callback_data=f"home {user_id}")],
        ]
        return button

    def userbot(user_id, count):
        button = [
            [
                InlineKeyboardButton(
                    "Hapus Dari Database",
                    callback_data=f"del_ubot {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Get Phone Number",
                    callback_data=f"get_phone {int(user_id)} {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Cek Masa Aktif",
                    callback_data=f"cek_masa_aktif {int(user_id)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Get Kode Otp",
                    callback_data=f"get_otp {int(user_id)} {int(count)}",
                )
            ],
            [
                InlineKeyboardButton(
                    "Get Kode 2fa",
                    callback_data=f"get_faktor {int(user_id)} {int(count)}",
                )
            ],
            [
                InlineKeyboardButton("⬅️", callback_data=f"prev_ub {int(count)}"),
                InlineKeyboardButton("➡️", callback_data=f"next_ub {int(count)}"),
            ],
        ]
        return button


class INLINE:
    def QUERY(func):
        async def wrapper(client, inline_query):
            users = ubot._get_my_id
            if inline_query.from_user.id not in users:
                await client.answer_inline_query(
                    inline_query.id,
                    cache_time=1,
                    results=[
                        (
                            InlineQueryResultArticle(
                                title=f"Lu Belum Beli Bot @{bot.me.username}",
                                input_message_content=InputTextMessageContent(f"Makannya Beli Dulu Jing Si @{bot.me.username} Biar Bisa Make Inline Ini"),
                            )
                        )
                    ],
                )
            else:
                await func(client, inline_query)

        return wrapper

    def DATA(func):
        async def wrapper(client, callback_query):
            users = ubot._get_my_id
            if callback_query.from_user.id not in users:
                await callback_query.answer(
                    f"ᴍᴀᴋᴀɴʏᴀ ᴏʀᴅᴇʀ ᴜsᴇʀʙᴏᴛ @{bot.me.username} ᴅᴜʟᴜ ʙɪᴀʀ ʙɪsᴀ ᴋʟɪᴋ ᴛᴏᴍʙᴏʟ ɪɴɪ",
                    True,
                )
            else:
                try:
                    await func(client, callback_query)
                except MessageNotModified:
                    await callback_query.answer("❌ ERROR")

        return wrapper
      

async def gcast_create_button(m):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    split_text = m.text.split("~", 1)
    for X in split_text[1].split():
        button_data = X.split("|", 1)
        button_label = button_data[0].replace("_", " ")
        button_url = button_data[1]
        keyboard.append(InlineKeyboardButton(button_label, url=button_url))
    buttons.add(*keyboard)
    text_button = split_text[0].split(None, 1)[1]
    return buttons, text_button


async def create_button(m):
    buttons = InlineKeyboard(row_width=1)
    keyboard = []
    msg = []
    if "~>" not in m.text.split(None, 1)[1]:
        for X in m.text.split(None, 1)[1].split():
            X_parts = X.split(":", 1)
            keyboard.append(InlineKeyboardButton(X_parts[0].replace("_", " "), url=X_parts[1]))
            msg.append(X_parts[0])
        buttons.add(*keyboard)
        if m.reply_to_message:
            text = m.reply_to_message.text
        else:
            text = " ".join(msg)
    else:
        for X in m.text.split("~>", 1)[1].split():
            X_parts = X.split(":", 1)
            keyboard.append(InlineKeyboardButton(X_parts[0].replace("_", " "), url=X_parts[1]))
        buttons.add(*keyboard)
        text = m.text.split("~>", 1)[0].split(None, 1)[1]

    return buttons, text


async def notes_create_button(text):
    buttons = InlineKeyboard(row_width=2)
    keyboard = []
    split_text = text.split("~>", 1)
    for X in split_text[1].split():
        split_X = X.split(":", 1)
        button_text = split_X[0].replace("_", " ")
        button_url = split_X[1]
        keyboard.append(InlineKeyboardButton(button_text, url=button_url))
    buttons.add(*keyboard)
    text_button = split_text[0]
    return buttons, text_button
