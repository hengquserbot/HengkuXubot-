import asyncio

from PyroUbot import *


async def spam_cmd(client, message):
    reply = message.reply_to_message
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    msg = await message.reply(f"<emoji id={proses}>⏳</emoji> Sedang Proses...", quote=False)
    if reply:
        try:
            count_message = int(message.command[1])
            for i in range(count_message):
                await reply.copy(message.chat.id)
                await asyncio.sleep(0.1)
        except Exception as error:
            return await msg.edit(str(error))
    else:
        if len(message.command) < 2:
            return await msg.edit("silahkan ketik <code>.help spam</code> untuk melihat cara menggunakan perintah ini")
        else:
            try:
                count_message = int(message.command[1])
                for i in range(count_message):
                    await message.reply(message.text.split(None, 2)[2], quote=False)
                    await asyncio.sleep(0.1)
            except Exception as error:
                return await msg.edit(str(error))
    await msg.delete()
    await message.delete()


async def dspam_cmd(client, message):
    reply = message.reply_to_message
    msg = await message.reply("Sedang Proses", quote=False)
    if reply:
        try:
            count_message = int(message.command[1])
            count_delay = int(message.command[2])
        except Exception as error:
            return await msg.edit(str(error))
        for i in range(count_message):
            try:
                await reply.copy(message.chat.id)
                await asyncio.sleep(count_delay)
            except:
                pass
    else:
        if len(message.command) < 4:
            return await msg.edit("Silahkan Ketik <code>.help spam</code> Untuk Melihat Cara Menggunakan Perintah Ini")
        else:
            try:
                count_message = int(message.command[1])
                count_delay = int(message.command[2])
            except Exception as error:
                return await msg.edit(str(error))
            for i in range(count_message):
                try:
                    await message.reply(message.text.split(None, 3)[3], quote=False)
                    await asyncio.sleep(count_delay)
                except:
                    pass
    await msg.delete()
    await message.delete()
