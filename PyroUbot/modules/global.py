from PyroUbot import *


__MODULE__ = "Gban"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Gban</b></blockquote>

<blockquote><b>๏ Perintah: {0}gban [User Id/Username/Reply User]
◉ Penjelasan:</b> Untuk Ban User Dari Semua Grup</b></blockquote>
<blockquote><b>๏ Perintah: {0}ungban [User Id/Usernsme/Reply User]
◉ Penjelasan: Untuk Unban User Dari Semua Grup</b></blockquote>
"""



@PY.UBOT("gban")
@PY.TOP_CMD
@ubot.on_message(filters.command(["Cgban"], "") & filters.user(DEVS))
async def global_banned(client, message):
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "6113872536968104754"
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "6113844439292054570"
    user_id, reason = await extract_user_and_reason(message)
    Tm = await message.reply(f"<b><emoji id={proses}>⏳</emoji> Siap Siap Ngilang Jing. . .</b>")
    if not user_id:
        return await Tm.edit(f"<b><emoji id={gagal}>❎</emoji> Loh Ga Ada Tolol</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    emoji_global = await get_vars(client.me.id, "EMOJI_GLOBAL") or "6172475875368373616"
    gban_user = await get_vars(client.me.id, "GBAN_USER") or "5971867376130461576"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "6113647841459047673"
    text = "<b>{} Global {}</b>\n\n<b>{} Berhasil: {} Chat</b>\n<b>{} Gagal: {} Chat</b>\n<b>{} User: <a href='tg://user?id={}'>{} {}</a></b>"
    if reason:
        text += "\n<b>Alasan:</b> {}"
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        ]:
            chat_id = dialog.chat.id
            if user.id == OWNER_ID:
                return await Tm.edit("Gabisaa Anjeng Gabisa Dia Yang Buat Gua Kontol")
            elif not user.id == OWNER_ID:
                try:
                    await client.ban_chat_member(chat_id, user.id)
                    done += 1
                    await asyncio.sleep(0.1)
                except:
                    failed += 1
                    await asyncio.sleep(0.1)
    await Tm.delete()
    return await message.reply(text.format(f"<emoji id={emoji_global}>💬</emoji>", "Banned", f"<emoji id={sukses}>✅</emoji>", done, f"<emoji id={gagal}>❎</emoji>", failed, f"<emoji id={gban_user}>👤</emoji>", user.id, user.first_name, (user.last_name or ""), reason))





@PY.UBOT("ungban")
@PY.TOP_CMD
@ubot.on_message(filters.command(["cungban"], "") & filters.user(DEVS))
async def global_unbanned(client, message):
    user_id = await extract_user(message)
    gagal = await get_vars(client.me.id, "EMOJI_GAGAL") or "5438630285635757876"
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    Tm = await message.reply(f"<b><emoji id={proses}>⏳</emoji></b> ᴍᴇᴍᴘʀᴏsᴇs. . .</b>")
    if not user_id:
        return await Tm.edit(f"<b><emoji id={gagal}>❎</emoji> ᴜsᴇʀ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    done = 0
    failed = 0
    emoji_global = await get_vars(client.me.id, "EMOJI_GLOBAL") or "6111585093220830556"
    gban_user = await get_vars(client.me.id, "GBAN_USER") or "6172475875368373616"
    sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
    text = "<b>{} Global {}</b>\n\n<b>{} Berhasil: {} Chat</b>\n<b>{} Gagal: {} Chat</b>\n<b>{} User: <a href='tg://user?id={}'>{} {}</a></b>"
    async for dialog in client.get_dialogs():
        chat_type = dialog.chat.type
        if chat_type in [
            ChatType.GROUP,
            ChatType.SUPERGROUP,
            ChatType.CHANNEL,
        ]:
            chat_id = dialog.chat.id
            try:
                await client.unban_chat_member(chat_id, user.id)
                done += 1
                await asyncio.sleep(0.1)
            except:
                failed += 1
                await asyncio.sleep(0.1)
    await Tm.delete()
    return await message.reply(text.format(f"<emoji id={emoji_global}>💬</emoji>", "Unbanned", f"<emoji id={sukses}>✅</emoji>", done, f"<emoji id={gagal}>❎</emoji>", failed, f"<emoji id={gban_user}>👤</emoji>", user.id, user.first_name, (user.last_name or "")))


