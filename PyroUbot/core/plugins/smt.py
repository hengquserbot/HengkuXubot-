import asyncio
import random

from pyrogram.raw.functions.messages import DeleteHistory

from PyroUbot import *


async def sg_cmd(client, message):
    get_user = await extract_user(message)
    lol = await message.reply("<blockquote><b>🔄 Sabar Ya Jink. . .</b></blockquote>")
    if not get_user:
        return await lol.edit("<blockquote><b>User Tidak Ditemukan</b></blockquote>")
    try:
        user_id = (await client.get_users(get_user)).id
    except Exception:
        try:
            user_id = int(message.command[1])
        except Exception as error:
            return await lol.edit(error)
    bot = ["@Sangmata_bot", "@SangMata_beta_bot"]
    getbot = random.choice(bot)
    await client.unblock_user(getbot)
    txt = await client.send_message(getbot, user_id)
    await asyncio.sleep(4)
    await txt.delete()
    await lol.delete()
    sg_name = [name.text async for name in client.search_messages(getbot, limit=2)]
    sg_name.reverse()
    for history in sg_name:
        if not history:
            await message.reply(f"❌ {getbot} Tidak Dapat Menerima Permintaan", quote=True)
        else:
            await message.reply(history, quote=True)
    user_info = await client.resolve_peer(getbot)
    return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
