import asyncio
from random import choice, shuffle
from pyrogram import emoji
from PyroUbot import get_arg 

tagallgcid = []


async def tagall_cmd(client, message):
    msg = await message.reply("Silahkan Tunggu", quote=True)

    tagallgcid.append(message.chat.id)
    emoji_list = [value for key, value in emoji.__dict__.items() if not key.startswith("__")]
    user_tagged = [f"<a href=tg://user?id={user.user.id}>{choice(emoji_list)}</a>" async for user in message.chat.get_members() if not (user.user.is_bot or user.user.is_deleted)]
    m = message.reply_to_message or message
    count = []
    for output in [user_tagged[i : i + 5] for i in range(0, len(user_tagged), 5)]:
        if message.chat.id not in tagallgcid:
            break
        try:
            await m.reply(
                f"{get_arg(message)}\n\n{' '.join(output)}",
                quote=bool(message.reply_to_message),
            )
            await asyncio.sleep(3)
            count += output
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await m.reply(
                f"{get_arg(message)}\n\n{' '.join(output)}",
                quote=bool(message.reply_to_message),
            )
            await asyncio.sleep(3)
            count += output

    await msg.delete()
    await message.reply(f"<b>✅ <code>{len(count)}</code> Anggota Berhasil Di Tag</b>")

    try:
        tagallgcid.remove(message.chat.id)
    except Exception:
        pass


async def batal_cmd(client, message):
    if message.chat.id not in tagallgcid:
        return await message.reply_text("sedang tidak ada perintah: <code>tagall</code> yang digunakan")
    try:
        tagallgcid.remove(message.chat.id)
    except Exception:
        pass
    await message.reply_text("ok tagall berhasil dibatalkan")
