import os
from asyncio import sleep

from pyrogram import Client, filters
from pyrogram.types import Message

from PyroUbot import *

__MODULE__ = "Profil"
__HELP__ = f"""
<blockquote><b>✘ Bantuan Untuk Profil

<blockquote><b>๏ Perintah: {0}setbio [Text]
◉ Penjelasan: Untuk Mengubah Bio Anda</b></blockquote>
<blockquote><b>๏ Perintah: {0}setname [Text]
◉ Penjelasan: Untuk Mengubah Nama Anda</b></blockquote>
<blockquote><b>๏ Perintah: {0}block [Reply To User]
◉ Penjelasan: Untuk Blokir Pengguna</b></blockquote>
<blockquote><b>๏ Perintah: {0}unblock [Reply To User]
◉ Penjelasan: Untuk Membuka Blokir</b></blockquote>
"""

@PY.UBOT("unblock")
@PY.TOP_CMD
async def unblock_user_func(client, message):
    user_id = await extract_user(message)
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.SUKSES(client)
    tex = await message.reply(f"<blockquote>{proses} Processing . . .</blockquote>")
    if not user_id:
        return await tex.edit(f"{gagal} Berikan Nama Atau Pengguna Yang Ingin Di Lepas Blockir.")
    if user_id == client.me.id:
        return await tex.edit(f"{sukses} Ok Done.")
    await client.unblock_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"<blockquote><b>{sukses} Berhasil Melepas Blockir Anak Jamet Ini {umention}</b></blockquote>")

@PY.UBOT("block")
@PY.TOP_CMD
async def block_user_func(client, message):
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.SUKSES(client)
    user_id = await extract_user(message)
    tex = await message.reply(f"<blockquote>{proses} Processing . . .</blockquote>")
    if not user_id:
        return await tex.edit(f"{gagal} Berikan Nama Pengguna Yang Ingin Di Blockir")
    if user_id == client.me.id:
        return await tex.edit(f"{sukses} Ok Done.")
    await client.block_user(user_id)
    umention = (await client.get_users(user_id)).mention
    await tex.edit(f"<blockquote>{sukses} <b>Berhasil Blockir Jamet Jelek Ini {umention}</b></blockquote>")

@PY.UBOT("setname")
@PY.TOP_CMD
async def setname(client: Client, message: Message):
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.SUKSES(client)
    tex = await message.reply(f"{proses} ᴍᴇᴍᴘʀᴏꜱᴇꜱ . . .")
    if len(message.command) == 1:
        return await tex.edit(f"{gagal} Berikan Text Untuk Digunakan Sebagai Nama Anda.")
    elif len(message.command) > 1:
        name = message.text.split(None, 1)[1]
        try:
            await client.update_profile(first_name=name)
            await tex.edit(
                f"<blockquote>{sukses} <b>Berhasil Mengubah Nama Menjadi <code>{name}</code></b></blockquote>"
            )
        except Exception as e:
            await tex.edit(f"{gagal} <b>ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit(f"<blockquote><b>{gagal} Berikan Teks Untuk Di Jadikan Nama Jelek Lu Itu.</b></blockquote>")

@PY.UBOT("setbio")
@PY.TOP_CMD
async def set_bio(client: Client, message: Message):
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.SUKSES(client)
    tex = await message.reply(f"<blockquote>{proses} Processing . . .</blockquote>")
    if len(message.command) == 1:
        return await tex.edit(f"<blockquote><b>{gagal} Berikan Teks Untuk Di Tetapkan Sebagai Bio.</b></blockquote>")
    elif len(message.command) > 1:
        bio = message.text.split(None, 1)[1]
        try:
            await client.update_profile(bio=bio)
            await tex.edit(f"<blockquote>{sukses} <b>Berhasil Mengubah Bio Menjadi <code>{bio}</code></b></blockquote>")
        except Exception as e:
            await tex.edit(f"{gagal} <b>ERROR:</b> <code>{e}</code>")
    else:
        return await tex.edit(f"<blockquote><b>{gagal} Berikan Teks Untuk Di Tetapkan Sebagai Bio.</b></blockquote>")
