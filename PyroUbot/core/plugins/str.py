import asyncio
import psutil
from datetime import datetime
from gc import get_objects
from time import time

from platform import python_version
from pyrogram import __version__

from pyrogram.raw.functions import Ping
from PyroUbot.core.database.max import get_uptime
from PyroUbot.core.helpers.uptime import get_time
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import *
from PyroUbot.config import START_IMG_URL
from PyroUbot.core.helpers import EMO

async def ping_cmd(client, message):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    delta_ping = (end - start).microseconds / 1000
    uptime = await get_time((time() - start_time))
    pong1 = await EMO.PING1(client)
    pong2 = await EMO.PING2(client)
    pong3 = await EMO.PING3(client)
    if client.me.is_premium:
        _ping = f"""
<blockquote><b>{pong1} Sepong:{int(delta_ping)} ms
{pong2} Uptime :{uptime}
{pong3} Pemake: <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b></blockquote>
"""
    else:
        _ping = f"""
<blockquote><b>🏓 Ping!! : {int(delta_ping)} ms
😎 Uptime : {uptime}
👤 User ~ <a href=tg://user?id={client.me.id}>{client.me.first_name} {client.me.last_name or ''}</a></b></blockquote>
"""
    await message.reply(_ping)


async def stats_ubot(client, message):
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    delta_ping = (end - start).microseconds / 1000
    delta_ping_formatted = round(delta_ping, 3)
    uptime = await get_time((time() - start_time))
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    buttons = [[InlineKeyboardButton("ʀᴇғʀᴇsʜ", callback_data="kontol")]]
    _ping = f"""
<blockquote><b>🖥️ [SYSTEM UBOT]
PING: {str(delta_ping_formatted).replace('.', ',')} ms
UBOT: {len(ubot._ubot)} user
UPTIME: {uptime}
OWNER: @pranwild</b> 

<b>📊 [STATUS SERVER]
CPU: {cpu}%
RAM: {mem}%
DISK: {disk}%
MEMORY: {round(process.memory_info()[0] / 1024 ** 2)} MB</b></blockquote>
"""
    await message.reply(_ping, reply_markup=InlineKeyboardMarkup(buttons))


async def cb_stats(client, callback_query):
    await callback_query.answer("ʀᴇғʀᴇsʜɪɴɢ...")
    start = datetime.now()
    await client.invoke(Ping(ping_id=0))
    end = datetime.now()
    delta_ping = (end - start).microseconds / 1000
    delta_ping_formatted = round(delta_ping, 3)
    uptime = await get_time((time() - start_time))
    cpu = psutil.cpu_percent()
    mem = psutil.virtual_memory().percent
    disk = psutil.disk_usage("/").percent
    process = psutil.Process(os.getpid())
    _ping = f"""
<blockquote><b>🖥️ [SYSTEM UBOT]
PING: {str(delta_ping_formatted).replace('.', ',')} ms
UBOT: {len(ubot._ubot)} user
UPTIME: {uptime}
OWNER: @pranwild</b> 

<b>📊 [STATUS SERVER]
CPU: {cpu}%
RAM: {mem}%
DISK: {disk}%
MEMORY: {round(process.memory_info()[0] / 1024 ** 2)} MB</b></blockquote>
"""
    buttons = [[InlineKeyboardButton("Refresh", callback_data="kontol")]]
    try:
        await callback_query.message.edit(_ping, reply_markup=InlineKeyboardMarkup(buttons))
    except:
        return


async def start_cmd(client, message):
    if len(message.command) < 2:
        buttons = Button.start(message)
        msg = MSG.START(message)
        photo = START_IMG_URL
        await message.reply(msg, photo, reply_markup=InlineKeyboardMarkup(buttons))
    else:
        txt = message.text.split(None, 1)[1]
        msg_id = txt.split("_", 1)[1]
        send = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ...</b>")
        if "secretMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ ᴇʀʀᴏʀ:</b> <code>{error}</code>")
            user_or_me = [m.reply_to_message.from_user.id, m.from_user.id]
            if message.from_user.id not in user_or_me:
                return await send.edit(f"<b>❌ ᴘᴇsᴀɴ ɪɴɪ ʙᴜᴋᴀɴ ᴜɴᴛᴜᴋᴍᴜ <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>")
            else:
                text = await client.send_message(
                    message.chat.id,
                    m.text.split(None, 1)[1],
                    protect_content=True,
                    reply_to_message_id=message.id,
                )
                await send.delete()
                await asyncio.sleep(120)
                await message.delete()
                await text.delete()
        elif "copyMsg" in txt:
            try:
                m = [obj for obj in get_objects() if id(obj) == int(msg_id)][0]
            except Exception as error:
                return await send.edit(f"<b>❌ ᴇʀʀᴏʀ:</b> <code>{error}</code>")
            id_copy = int(m.text.split()[1].split("/")[-1])
            if "t.me/c/" in m.text.split()[1]:
                chat = int("-100" + str(m.text.split()[1].split("/")[-2]))
            else:
                chat = str(m.text.split()[1].split("/")[-2])
            try:
                get = await client.get_messages(chat, id_copy)
                await get.copy(message.chat.id, reply_to_message_id=message.id)
                await send.delete()
            except Exception as error:
                await send.edit(error)
