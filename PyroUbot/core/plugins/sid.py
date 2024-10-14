from pyrogram.enums import ChatType

from PyroUbot import *


async def id_cmd(client, message):
    text = f"<blockquote><b><emoji id=5319302904308309833>◎</emoji><a href={message.link}>Message Id:</a> <code>{message.id}</code></b></blockquote>\n"

    if message.chat.type == ChatType.CHANNEL:
        text += f"<blockquote><b><emoji id=5319139772860472979>◎</emoji><a href=https://t.me/{message.chat.username}>Chat Id:</a> <code>{message.sender_chat.id}</code></b></blockquote>\n"
    else:
        text += f"<blockquote><b><emoji id=5318967574736676420>◎</emoji><a href=tg://user?id={message.from_user.id}>Your Id:</a> <code>{message.from_user.id}</code></b></blockquote>\n"

        if len(message.command) > 1:
            try:
                user = await client.get_chat(message.text.split()[1])
                text += f"<blockquote><b><emoji id=5321238272406461248>◎</emoji><a href=tg://user?id={user.id}>User Id:</a> <code>{user.id}</code></b></blockquote>\n\n"
            except BaseException:
                return await message.reply("<blockquote>Pengguna tidak ditemukan.</blockquote>")

        text += f"<blockquote><b><emoji id=5319139772860472979>◎</emoji> <a href=https://t.me/{message.chat.username}>Chat Id:</a> <code>{message.chat.id}</code></b></blockquote>\n\n"

    if message.reply_to_message:
        id_ = (
            message.reply_to_message.from_user.id
            if message.reply_to_message.from_user
            else message.reply_to_message.sender_chat.id
        )
        file_info = get_file_id(message.reply_to_message)
        if file_info:
            text += f"<blockquote><b><emoji id=5318967574736676420>◎</emoji><a href={message.reply_to_message.link}>Media Id:</a> <code>{file_info.file_id}</code></b></blockquote>\n\n"
        text += (
            f"<blockquote><b><emoji id=5321238272406461248>◎</emoji><a href={message.reply_to_message.link}>Replied Message Id:</a></b> <code>{message.reply_to_message.id}</code></b></blockquote>\n"
            f"<blockquote><b><emoji id=5319139772860472979>◎</emoji><a href=tg://user?id={id_}>Replied User Id:</a> <code>{id_}</code></b></blockquote>"
        )

    return await message.reply(text, disable_web_page_preview=True)
