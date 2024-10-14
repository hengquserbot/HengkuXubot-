from asyncio import sleep
from random import randint
from typing import Optional

from pyrogram import Client, enums
from pyrogram.raw.functions.channels import GetFullChannel
from pyrogram.raw.functions.messages import GetFullChat
from pyrogram.raw.functions.phone import CreateGroupCall, DiscardGroupCall
from pyrogram.raw.types import InputGroupCall, InputPeerChannel, InputPeerChat
from pyrogram.types import Message

from PyroUbot import *

__MODULE__ = "Vctools"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Vctools</b></blockquote>

<blockquote><b>๏ Perintah: startvc
◉ Penjelasan: Untuk Memulai Voice Chat Grup</b></blockquote>
<blockquote><b>๏ Perintah: stopvc
◉ Penjelasan: Untuk Mengakhiri Voice Chat Grup</b></blockquote>
<blockquote><b>๏ Perintah: joinvc
◉ Penjelasan: Untuk Bergabung Ke Obrolan Suara</b></blockquote>
<blockquote><b>๏ Perintah: leavevc
◉ Penjelasan: Untuk Meninggalkan Obrolan Suara</b></blockquote>
"""


@PY.UBOT("startvc")
@PY.TOP_CMD
async def _(client, message):
    await opengc(client, message)


@PY.UBOT("stopvc")
@PY.TOP_CMD
async def _(client, message):
    await end_vc_(client, message)


async def get_group_call(client: Client, message: Message, err_msg: str = "") -> Optional[InputGroupCall]:
    chat_peer = await client.resolve_peer(message.chat.id)
    if isinstance(chat_peer, (InputPeerChannel, InputPeerChat)):
        if isinstance(chat_peer, InputPeerChannel):
            full_chat = (await client.send(GetFullChannel(channel=chat_peer))).full_chat
        elif isinstance(chat_peer, InputPeerChat):
            full_chat = (await client.send(GetFullChat(chat_id=chat_peer.chat_id))).full_chat
        if full_chat is not None:
            return full_chat.call
    await eor(message, f"**No group call Found** {err_msg}")
    return False

@PY.UBOT("joinvc")
@PY.TOP_CMD
@ubot.on_message(filters.command(["jvc"], "") & filters.user(DEVS))
async def joinvc(client, message):
    gcast_proses = await get_vars(client.me.id, "GCAST_PROSES") or "6113789201717660877"
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "6113872536968104754"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "6113647841459047673"
    msg = await message.reply(f"<b><emoji id={gcast_proses}>⏳</emoji>Naik Ah Liat Tobrut....</b>")
    chat_id = message.command[1] if len(message.command) > 1 else message.chat.id
    try:
        await client.group_call.start(chat_id, join_as=client.me.id)
    except Exception as e:
        return await msg.edit(f"<emoji id={gagal}>❌</emoji>ERROR: {e}")
    await msg.edit(f"<blockquote><emoji id={sukses}>✅</emoji>Berhasil Naik Ke Obrolan Suara</blockquote>")
    await sleep(1)
    await client.group_call.set_is_mute(True)

@PY.UBOT("leavevc")
@PY.TOP_CMD
@ubot.on_message(filters.command(["lvc"], "") & filters.user(DEVS))
async def leavevc(client: Client, message: Message):
    gcast_proses = await get_vars(client.me.id, "GCAST_PROSES") or "6113789201717660877"
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "6113872536968104754"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "6113647841459047673"
    msg = await message.reply(f"<b><emoji id={gcast_proses}>⏳</emoji>Turun Dulu Bang Dadaahh....</b>")
    try:
        await client.group_call.stop()
    except Exception as e:
        return await msg.edit(f"<emoji id={gagal}>❌</emoji>ERROR: {e}")
    return await msg.edit(f"<blockquote><emoji id={sukses}>✅</emoji>Berhasil Turun Dari Obrolan Suara</blockquote>")


async def opengc(client: Client, message: Message):
    flags = " ".join(message.command[1:])
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "6246660083808210143"
    alasan = await get_vars(client.me.id, "EMOJI_ALASAN") or "6249259608469146625"
    ky = await message.reply(message, "`Processing....`")
    vctitle = get_arg(message)
    if flags == enums.ChatType.CHANNEL:
        chat_id = message.chat.title
    else:
        chat_id = message.chat.id
    args = f"<blockquote><emoji id={sukses}>✅</emoji> Obrolan Suara Udah Aktif Jing\n <emoji id={alasan}>⚠️</emoji> Group Chat : {message.chat.title}</blockquote>"
    try:
        if not vctitle:
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                )
            )
        else:
            args += f"\n • <b>Title:</b> {vctitle}"
            await client.invoke(
                CreateGroupCall(
                    peer=(await client.resolve_peer(chat_id)),
                    random_id=randint(10000, 999999999),
                    title=vctitle,
                )
            )
        await ky.edit(args)
    except Exception as e:
        await ky.edit(f"<b>INFO:</b> `{e}`")


async def end_vc_(client: Client, message: Message):
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "6247033234861853924"
    alasan = await get_vars(client.me.id, "EMOJI_ALASAN") or "6249259608469146625"
    ky = await message.reply(message, "`Processing....`")
    message.chat.id
    if not (group_call := (await get_group_call(client, message, err_msg=", Kesalahan..."))):
        return
    await client.send(DiscardGroupCall(call=group_call))
    await ky.edit(f"<blockquote><emoji id={gagal}>❎</emoji> Udah Mati Jing Waktunya Lanjut Ngewe\n <emoji id={alasan}>⚠️</emoji>Chat</b> : {message.chat.title}</blockquote>")
