import asyncio

from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import *

SUPPORT = []


async def support_callback(client, callback_query):
    user_id = int(callback_query.from_user.id)
    full_name = f"{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}"
    get = await bot.get_users(user_id)
    await callback_query.message.delete()
    SUPPORT.append(get.id)
    try:
        button = [[InlineKeyboardButton("Batalkan", callback_data=f"batal {user_id}")]]
        pesan = await bot.ask(
            user_id,
            f"<b>Silahkan Kirim Pertanyaan Anda: {full_name}</b>",
            reply_markup=InlineKeyboardMarkup(button),
            timeout=90,
        )
    except asyncio.TimeoutError as out:
        if get.id in SUPPORT:
            SUPPORT.remove(get.id)
            return await bot.send_message(get.id, "Pembatalan Otomatis")
    text = f"<blockquote><b>Pertanyaan Sudah Terkirim: {full_name}</b></blockquote>"
    buttons = [
        [
            InlineKeyboardButton("Profil", callback_data=f"profil {user_id}"),
            InlineKeyboardButton("Jawab", callback_data=f"jawab_pesan {user_id}"),
        ],
    ]
    if get.id in SUPPORT:
        try:
            await pesan.copy(
                OWNER_ID,
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            SUPPORT.remove(get.id)
            await pesan.request.edit(f"<blockquote><b>Silahkan Kirim Pertanyaan Anda: {full_name}</b></blockquote>")
            return await bot.send_message(user_id, text)
        except Exception as error:
            return await bot.send_message(user_id, error)


async def jawab_pesan_callback(client, callback_query):
    user_id = int(callback_query.from_user.id)
    full_name = f"{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}"
    get = await bot.get_users(user_id)
    user_ids = int(callback_query.data.split()[1])
    SUPPORT.append(get.id)
    try:
        button = [[InlineKeyboardButton("Batalkan", callback_data=f"batal {user_id}")]]
        pesan = await bot.ask(
            user_id,
            f"<b>Silahkan Kirim Balasan Anda: {full_name}</b>",
            reply_markup=InlineKeyboardMarkup(button),
            timeout=300,
        )
    except asyncio.TimeoutError:
        if get.id in SUPPORT:
            SUPPORT.remove(get.id)
            return await bot.send_message(get.id, "Pembatalan Otomatis")
    text = f"<blockquote><b>Pesan Balasan Anda Telah Terikirim: {full_name}</b></blockquote>"
    if not user_ids == OWNER_ID:
        buttons = [[InlineKeyboardButton("Jawab Pesan", f"jawab_pesan {user_id}")]]
    else:
        buttons = [
            [
                InlineKeyboardButton("Profil", callback_data=f"profil {user_id}"),
                InlineKeyboardButton("Jawab", callback_data=f"jawab_pesan {user_id}"),
            ],
        ]
    if get.id in SUPPORT:
        try:
            await pesan.copy(
                user_ids,
                reply_markup=InlineKeyboardMarkup(buttons),
            )
            SUPPORT.remove(get.id)
            await pesan.request.edit(
                f"<blockquote><b>Silahkan Kirim Balasan Anda: {full_name}</b></blockquote>",
            )
            await bot.send_message(user_id, text)
        except Exception as error:
            return await bot.send_message(user_id, error)


async def profil_callback(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    try:
        get = await bot.get_users(user_id)
        first_name = f"{get.first_name}"
        last_name = f"{get.last_name}"
        full_name = f"{get.first_name} {get.last_name or ''}"
        username = f"{get.username}"
        msg = f"<b>👤 <a href=tg://user?id={get.id}>{full_name}</a></b>\n" f"<b> ┣ Id Pengguna:</b> <code>{get.id}</code>\n" f"<b> ┣ Nama Depan:</b> {first_name}\n"
        if last_name == "None":
            msg += ""
        else:
            msg += f"<b> ┣ Nama Belakang:</b> {last_name}\n"
        if username == "None":
            msg += ""
        else:
            msg += f"<b> ┣ Username:</b> @{username}\n"
        msg += f"<b> ┗ Userbot: {bot.me.mention}\n"
        buttons = [
            [
                InlineKeyboardButton(
                    f"{full_name}",
                    url=f"tg://openmessage?user_id={get.id}",
                )
            ]
        ]
        await callback_query.message.reply_text(msg, reply_markup=InlineKeyboardMarkup(buttons))
    except Exception as why:
        await callback_query.message.reply_text(why)


async def batal_callback(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    if user_id in SUPPORT:
        try:
            SUPPORT.remove(user_id)
            await callback_query.message.delete()
            buttons = Button.start(callback_query)
            return await bot.send_message(
                user_id,
                MSG.START(callback_query),
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        except Exception as why:
            await callback_query.message.delete()
            await bot.send_message(user_id, f"<b>Gagal Dibatalkan! {why}</b>")
