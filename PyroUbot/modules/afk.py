from time import time

from PyroUbot import *

__MODULE__ = "Afk"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Afk</b></blockquote>

<blockquote><b>๏ Perintah: afk
◉ Penjelasan: <u>Untuk Mengaktifkan Afk</u></b></blockquote>
<blockquote><b>๏ Perintah: unafk
◉ Penjelasan: <u>Untuk Menonaktifkan Afk</u></b></blockquote>
"""


@PY.UBOT("afk")
@PY.TOP_CMD
async def _(client, message):
    reason = get_arg(message)
    db_afk = {"time": time(), "reason": reason}
    emot_1 = await get_vars(client.me.id, "EMOJI_AFK")
    emot_2 = await get_vars(client.me.id, "EMOJI_REASON")
    emot_afk = emot_1 if emot_1 else "6113647841459047673"
    emot_reason = emot_2 if emot_2 else "5368439585032380899"
    if client.me.is_premium:
        msg_afk = f"<b><emoji id={emot_afk}>🦇</emoji> Sedang Afk\n<emoji id={emot_reason}>📝</emoji> Alasan: {reason}</b>" if reason else f"<b><emoji id={emot_afk}>‼️</emoji> Sedang Afk</b>"
    else:
        msg_afk = f"<b>Sedang Afk\nAlasan: {reason}</b>" if reason else "<b>Sedang Afk</b>"
    await set_vars(client.me.id, "AFK", db_afk)
    await message.reply(msg_afk)
    return await message.delete()


@PY.AFK()
async def _(client, message):
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        afk_time = vars.get("time")
        afk_reason = vars.get("reason")
        afk_runtime = await get_time(time() - afk_time)
        emot_1 = await get_vars(client.me.id, "EMOJI_AFK")
        emot_2 = await get_vars(client.me.id, "EMOJI_REASON")
        emot_3 = await get_vars(client.me.id, "EMOJI_WAKTU")
        emot_afk = emot_1 if emot_1 else "6113647841459047673"
        emot_reason = emot_2 if emot_2 else "5368439585032380899"
        emot_waktu = emot_3 if emot_3 else "6186224886021622832"
        if client.me.is_premium:
            afk_text = f"<b><emoji id={emot_afk}>🦇</emoji> Sedang Afk\n<emoji id={emot_waktu}>⏰</emoji> Waktu: {afk_runtime}\n<emoji id={emot_reason}>🏓</emoji> Alasan: {afk_reason}</b>" if afk_reason else f"<b><emoji id={emot_afk}>🦇</emoji> Sedang Afk\n<emoji id={emot_waktu}>⏰</emoji> Waktu: {afk_runtime}</b>"
        else:
            afk_text = f"<b>Sedang Afk\nWaktu: {afk_runtime}\nAlasan: {afk_reason}</b>" if afk_reason else f"<b>Sedang Afk\nWaktu: {afk_runtime}</b>"
        return await message.reply(afk_text)


@PY.UBOT("unafk")
@PY.TOP_CMD
async def _(client, message):
    vars = await get_vars(client.me.id, "AFK")
    if vars:
        emot_1 = await get_vars(client.me.id, "EMOJI_AFK")
        emot_3 = await get_vars(client.me.id, "EMOJI_WAKTU")
        afk_time = vars.get("time")
        afk_runtime = await get_time(time() - afk_time)
        emot_afk = emot_1 if emot_1 else "6113647841459047673"
        emot_waktu = emot_3 if emot_3 else "6186224886021622832"
        afk_text = f"<b><emoji id={emot_afk}>🦇</emoji> Duar Memek Gua Balik Nih\n<emoji id={emot_waktu}>⏰</emoji> Afk Selama: {afk_runtime}</b>"
        await message.reply(afk_text)
        await message.delete()
        return await remove_vars(client.me.id, "AFK")
