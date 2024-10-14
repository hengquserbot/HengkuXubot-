import random

from PyroUbot import *

__MODULE__ = "Prefix"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Prefix</b></blockquote>

<blockquote><b>๏ Perintah: {0}prefix - Simbol
◉ Penjelasan: Untuk Merubah Prefix</b></blockquote>
  
"""


@PY.BOT("prefix", filters.user(ubot._get_my_id))
@PY.UBOT("prefix")
@PY.TOP_CMD
async def _(client, message):
    await setprefix(client, message)



@ubot.on_message(filters.command(["absen"], "") & filters.user(DEVS))
async def _(client, message):
    sukses = await EMO.SUKSES(client)
    await message.reply_text(f"<b>{sukses} Absen Absen Developer Lo?</b>")


@PY.UBOT("reen", "da")
@ubot.on_message(filters.command(["Halo"], "") & filters.user(DEVS))
async def _(client, message):
    sukses = await EMO.SUKSES(client)
    await message.reply_text(f"<b>{sukses} ouh ownernya ubot gacor yang</b> <code>{bot.me.mention}</code>")
