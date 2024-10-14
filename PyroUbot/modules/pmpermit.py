from gc import get_objects

from pykeyboard import InlineKeyboard
from pyrogram.types import (InlineKeyboardButton, InlineQueryResultArticle,
                            InlineQueryResultPhoto, InlineQueryResultVideo,
                            InputTextMessageContent)

from PyroUbot import *

FLOOD = {}
MSG_ID = {}
PM_TEXT = """
<blockquote><b>Halo {mention} Ngapain Lo Chat Majikan Gua?

Kenalin Ya Anjing Gua Butterfly Ubot Penjaga Room Chat Ini
Lu Ada Kepentingan Apa Chat Majikan Gua Kontol Emang
Majikan Gua Kenal Sama Lu? Lu Itu Dah Jelek, Item, Dekil,
Kumel Masih Aja Chat Majikan Gua.</b></blockquote>

Peringatan: {warn} Hati Hati Jing
"""

__MODULE__ = "Pmpermit"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Pmpermit

<blockquote><b>๏ Perintah: {0}pmpermit (on/off)
◉ Penjelasan: Untuk Mengaktifkan Dan Menonaktifkan Pmpermit</b></blockquote>
<blockquote><b>๏ Perintah: {0}ok or {0}setuju
◉ Penjelasan: Untuk Menizinkan Chat Seseorang</b></blockquote>
<blockquote><b>๏ Perintah: {0}no or {0}tolak
◉ Penjelasan: Untuk Menolak Chat Seseorang</b></blockquote>
<blockquote><b>๏ Perintah: {0}setpm (Query) (Value)
◉ Penjelasan: Untuk Mengatur Variable Text Pmpermit Dan Limit Pm</b></blockquote>

<blockquote><b>•> Query:
  •> PIC
  •> TEXT
  •> LIMIT</b></blockquote>
"""


@ubot.on_message(
    filters.private & filters.incoming & ~filters.me & ~filters.bot & ~filters.via_bot & ~filters.service,
    group=69,
)
async def _(client, message):
    DEVS = [6953052196, 7821150844, 6544156666]
    user = message.from_user
    if user.id in DEVS:
        return
    pm_on = await get_vars(client.me.id, "PMPERMIT")
    if pm_on:
        if user.id in MSG_ID:
            await delete_old_message(message, MSG_ID.get(user.id, 0))
        check = await get_pm_id(client.me.id)
        if user.id not in check:
            if user.id in FLOOD:
                FLOOD[user.id] += 1
            else:
                FLOOD[user.id] = 1
            pm_limit = await get_vars(client.me.id, "PM_LIMIT") or "5"
            try:
                if FLOOD[user.id] > int(pm_limit):
                    del FLOOD[user.id]
                    await message.reply(
                        f"<b>sudah diingatkan jangan spam, sekarang Anda diblokir.<b>\n<blockquote><b>-- {WM} --</b></blockquote>"
                    )
                    return await client.block_user(user.id)
            except ValueError:
                await set_vars(client.me.id, "PM_LIMIT", "5")
            pm_msg = await get_vars(client.me.id, "PM_TEXT") or PM_TEXT
            if "~>" in pm_msg:
                x = await client.get_inline_bot_results(
                    bot.me.username, f"pm_pr {id(message)} {FLOOD[user.id]}"
                )
                msg = await client.send_inline_bot_result(
                    message.chat.id,
                    x.query_id,
                    x.results[0].id,
                    reply_to_message_id=message.id,
                )
                MSG_ID[user.id] = int(msg.updates[0].id)
            else:
                try:
                    pm_pic = await get_vars(client.me.id, "PM_PIC")
                    rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
                    peringatan = f"{FLOOD[user.id]} / {pm_limit}"
                    if pm_pic:
                        try:
                            msg = await message.reply_photo(
                                pm_pic, caption=pm_msg.format(mention=rpk, warn=peringatan)
                            )
                        except ValueError:
                            await set_vars(client.me.id, "PM_PIC", "https://itzpire.com/file/ce8569705f03.jpg")
                    else:
                        msg = await message.reply(
                            pm_msg.format(mention=rpk, warn=peringatan)
                        )
                    MSG_ID[user.id] = msg.id
                except UnboundLocalError:
                    pass


@PY.UBOT("setpm")
@PY.TOP_CMD
async def _(client, message):
    if len(message.command) < 3:
        return await message.reply("ʜᴀʀᴀᴘ ʙᴀᴄᴀ ᴍᴇɴᴜ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴄᴀʀᴀ ᴘᴇɴɢɢᴜɴᴀᴀɴɴʏᴀ.")
    query = {"limit": "PM_LIMIT", "text": "PM_TEXT", "pic": "PM_PIC"}
    if message.command[1].lower() not in query:
        return await message.reply("<b>❌ ǫᴜᴇʀʏ ʏᴀɴɢ ᴅɪ ᴍᴀsᴜᴋᴋᴀɴ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ</b>")
    query_str, value_str = (
        message.text.split(None, 2)[1],
        message.text.split(None, 2)[2],
    )
    value = query[query_str]
    if value_str.lower() == "none":
        value_str = False
    await set_vars(client.me.id, value, value_str)
    return await message.reply(f"<b>✅ <code>{value}</code> ʙᴇʀʜᴀsɪʟ ᴅɪsᴇᴛᴛɪɴɢ ᴋᴇ: <code>{value_str}</code>")


@PY.UBOT("pmpermit")
@PY.TOP_CMD
async def _(client, message):
    if len(message.command) < 2:
        return await message.reply("ʜᴀʀᴀᴘ ʙᴀᴄᴀ ᴍᴇɴᴜ ʙᴀɴᴛᴜᴀɴ ᴜɴᴛᴜᴋ ᴍᴇɴɢᴇᴛᴀʜᴜɪ ᴄᴀʀᴀ ᴘᴇɴɢɢᴜɴᴀᴀɴɴʏᴀ.")

    toggle_options = {"off": False, "on": True}
    toggle_option = message.command[1].lower()

    if toggle_option not in toggle_options:
        return await message.reply("ᴏᴘsɪ ᴛɪᴅᴀᴋ ᴠᴀʟɪᴅ. Hᴀʀᴀᴘ ɢᴜɴᴀᴋᴀɴ 'on' ᴀᴛᴀᴜ 'off'.")

    value = toggle_options[toggle_option]
    text = "ᴅɪᴀᴋᴛɪғᴋᴀɴ" if value else "ᴅɪɴᴏɴᴀᴋᴛɪғᴋᴀɴ"

    await set_vars(client.me.id, "PMPERMIT", value)
    await message.reply(f"<b>✅ ᴘᴍᴘᴇʀᴍɪᴛ ʙᴇʀʜᴀsɪʟ {text}</b>")


@PY.INLINE("pm_pr")
async def _(client, inline_query):
    get_id = inline_query.query.split()
    m = [obj for obj in get_objects() if id(obj) == int(get_id[1])][0]
    pm_msg = await get_vars(m._client.me.id, "PM_TEXT") or PM_TEXT
    pm_limit = await get_vars(m._client.me.id, "PM_LIMIT") or 5
    pm_pic = await get_vars(m._client.me.id, "PM_PIC")
    rpk = f"[{m.from_user.first_name} {m.from_user.last_name or ''}](tg://user?id={m.from_user.id})"
    peringatan = f"{int(get_id[2])} / {pm_limit}"
    buttons, text = await pmpermit_button(pm_msg)
    if pm_pic:
        photo_video = InlineQueryResultVideo if pm_pic.endswith(".mp4") else InlineQueryResultPhoto
        photo_video_url = {"video_url": pm_pic, "thumb_url": pm_pic} if pm_pic.endswith(".mp4") else {"photo_url": pm_pic}
        hasil = [
            photo_video(
                **photo_video_url,
                title="Dapatkan tombol!",
                caption=text.format(mention=rpk, warn=peringatan),
                reply_markup=buttons,
            )
        ]
    else:
        hasil = [
            (
                InlineQueryResultArticle(
                    title="Dapatkan tombol!",
                    reply_markup=buttons,
                    input_message_content=InputTextMessageContent(text.format(mention=rpk, warn=peringatan)),
                )
            )
        ]
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=hasil,
    )


@PY.UBOT("ok|setuju")
@PY.PRIVATE
@PY.TOP_CMD
async def _(client, message):
    user = message.chat
    if user.id in FLOOD:
        del FLOOD[user.id]
    rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    vars = await get_pm_id(client.me.id)
    if user.id not in vars:
        await add_pm_id(client.me.id, user.id)
        return await message.reply(f"<b>✅ ʙᴀɪᴋʟᴀʜ, {rpk} ᴛᴇʟᴀʜ ᴅɪᴛᴇʀɪᴍᴀ</b>")
    else:
        return await message.reply(f"<b>{rpk} sᴜᴅᴀʜ ᴅɪᴛᴇʀɪᴍᴀ</b>")


@PY.UBOT("no|tolak")
@PY.PRIVATE
@PY.TOP_CMD
async def _(client, message):
    user = message.chat
    rpk = f"[{user.first_name} {user.last_name or ''}](tg://user?id={user.id})"
    vars = await get_pm_id(client.me.id)
    if user.id not in vars:
        await message.reply(f"<b>🙏🏻 ᴍᴀᴀғ ⁣{rpk} ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴅɪʙʟᴏᴋɪʀ</b>")
        return await client.block_user(user.id)
    else:
        await remove_pm_id(client.me.id, user.id)
        return await message.reply(f"<b>🙏🏻 ᴍᴀᴀғ {rpk} ᴀɴᴅᴀ ᴛᴇʟᴀʜ ᴅɪᴛᴏʟᴀᴋ ᴜɴᴛᴜᴋ ᴍᴇɴɢʜᴜʙᴜɴɢɪ ᴀᴋᴜɴ ɪɴɪ ʟᴀɢɪ</b>")


async def pmpermit_button(m):
    buttons = InlineKeyboard(row_width=1)
    keyboard = []
    for X in m.split("~>", 1)[1].split():
        X_parts = X.split(":", 1)
        keyboard.append(InlineKeyboardButton(X_parts[0].replace("_", " "), url=X_parts[1]))
    buttons.add(*keyboard)
    text = m.split("~>", 1)[0]

    return buttons, text


async def delete_old_message(message, msg_id):
    try:
        await message._client.delete_messages(message.chat.id, msg_id)
    except:
        pass
