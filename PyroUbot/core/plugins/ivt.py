import asyncio

from pyrogram.enums import UserStatus

from PyroUbot import *


async def invite_cmd(client, message):
    mg = await message.reply("<blockquote><b>Menambahkan Pengguna!</b></blockquote>")
    if len(message.command) < 2:
        return await mg.delete()
    user_s_to_add = message.text.split(" ", 1)[1]
    if not user_s_to_add:
        await mg.edit("<blockquote><b>Beri Saya Pengguna Untuk Di Tambahkan! Periksa Menu Bantuan Untuk Info Lebih Lanjut!!</b></blockquote>")
        return
    user_list = user_s_to_add.split(" ")
    try:
        await client.add_chat_members(message.chat.id, user_list, forward_limit=100)
    except Exception as e:
        return await mg.edit(f"{e}")
    await mg.edit(f"<blockquote><b>Berhasil Di Tambahkan {len(user_list)} Ke Group Ini</b></blockquote>")


invite_id = []


async def inviteall_cmd(client, message):
    Tm = await message.reply("<blockquote><b>🔄 Sabar Ya Jink...</b></blockquote>")
    if len(message.command) < 3:
        await message.delete()
        return await Tm.delete()
    try:
        chat = await client.get_chat(message.command[1])
    except Exception as error:
        return await Tm.edit(error)
    if message.chat.id in invite_id:
        return await Tm.edit_text(f"<blockquote><b>Sedang Meng Invite Member Silahkan Coba Lagi Nanti Atau Gunakan Perintah: <code>{PREFIX[0]}cancel</code></b></blockquote>")
    else:
        done = 0
        failed = 0
        invite_id.append(message.chat.id)
        await Tm.edit_text(f"<blockquote><b>Mengundang Anggota Dari {chat.title}</b></blockquote>")
        async for member in client.get_chat_members(chat.id):
            stats = [
                UserStatus.ONLINE,
                UserStatus.OFFLINE,
                UserStatus.RECENTLY,
                UserStatus.LAST_WEEK,
            ]
            if member.user.status in stats:
                try:
                    await client.add_chat_members(message.chat.id, member.user.id)
                    done = done + 1
                    await asyncio.sleep(int(message.command[2]))
                except Exception:
                    failed = failed + 1
                    await asyncio.sleep(int(message.command[2]))
        invite_id.remove(message.chat.id)
        await Tm.delete()
        return await message.reply(
            f"""
<blockquote><b>✅ <code>{done}</code> Anggota Yang Berhasil Di Undang
❌ <code>{failed}</code> Anggota Yang Gagal Di Undang</b></blockquote>
"""
        )


async def cancel_cmd(client, message):
    if message.chat.id not in invite_id:
        return await message.reply_text(f"Sedang Tidak Ada Perintah: <code>{0}inviteall</code> Yang Di Gunakan")
    try:
        invite_id.remove(message.chat.id)
        await message.reply_text("ok inviteall berhasil dibatalkan")
    except Exception as e:
        await message.reply_text(e)
