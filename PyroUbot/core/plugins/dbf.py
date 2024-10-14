from datetime import datetime, timedelta

from dateutil.relativedelta import relativedelta
from pyrogram.enums import ChatType
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone

from PyroUbot import *
from PyroUbot.core.helpers import EMO

# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℙℝ𝔼𝕄𝕀𝕌𝕄 #
# ========================== #


async def prem_user(client, message):
    proses = await EMO.PROSES(client)
    Tm = await message.reply(f"<pre>{proses} Processing . . .</pre>")
    if message.from_user.id not in await get_seles():
        return await Tm.edit("<blockquote><b>Untuk Menggunakan Perintah Ini Anda Harus Menjadi Reseller Terlebih Dahulu</b></blockquote>")
    user_id, get_bulan = await extract_user_and_reason(message)
    if not user_id:
        gagal = await EMO.GAGAL(client)
        return await Tm.edit(f"<blockquote><b>{gagal} {message.text} User_Id/Username - Bulan</b></blockquote>")
    try:
        get_id = (await client.get_users(user_id)).id
    except Exception as error:
        return await Tm.edit(error)
    if not get_bulan:
        get_bulan = 1
    premium = await get_prem()
    if get_id in premium:
        gagal = await EMO.GAGAL(client)
        return await Tm.edit(f"<blockquote><b>{gagal} Dia Sudah Bisa Membuat Userbot</b></blockquote>")
    added = await add_prem(get_id)
    if added:
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(get_bulan))
        await set_expired_date(get_id, expired)
        sukses = await EMO.SUKSES(client)
        alasan = await EMO.ALASAN(client)
        await Tm.edit(f"<blockquote><b>{sukses} {get_id} Telah Di Aktifkan Selama {get_bulan} Bulan\n\n{alasan} Silahkan Buat Userbot Di @{bot.me.username}</b></blockquote>")
        await bot.send_message(
            OWNER_ID,
            f"• {message.from_user.id} ─> {get_id} •",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Profil",
                            callback_data=f"profil {message.from_user.id}",
                        ),
                        InlineKeyboardButton("Profil", callback_data=f"profil {get_id}"),
                    ],
                ]
            ),
        )
    else:
        await Tm.delete()
        await message.reply_text("Terjadi Kesalahan Seng Mboh Ra Eroh")


async def unprem_user(client, message):
    proses = await EMO.SUKSES(client)
    user_id = await extract_user(message)
    Tm = await message.reply(f"<blockquote><b>{proses} Processing . . .</b></blockquote>")
    if not user_id:
        return await Tm.edit("<blockquote><b>Balas Pesan Pengguna Atau Berikan User Id/Username</b></blockquote>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    delpremium = await get_prem()
    if user.id not in delpremium:
        return await Tm.edit("<b>Ga Ketemu Tolol</b>")
    removed = await remove_prem(user.id)
    if removed:
        sukses = await EMO.SUKSES(client)
        await Tm.edit(f"<b> {sukses} {user.mention} Berhasil Di Buang</b>")
    else:
        await Tm.delete()
        await message.reply_text("Terjadi Kesalahan Jing Gatau Dimana")


async def get_prem_user(client, message):
    text = ""
    count = 0
    for user_id in await get_prem():
        try:
            user = await bot.get_users(user_id)
            count += 1
            userlist = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"{userlist}\n"
    if not text:
        await message.reply_text("Tidak Ada Pengguna Yang Di Temukan")
    else:
        await message.reply_text(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔹𝕃𝔸ℂ𝕂𝕃𝕀𝕊𝕋 #
# ========================== #


async def add_blacklist(client, message):
    proses = await EMO.PROSES(client)
    Tm = await message.reply(f"<b>{proses} Sabar Jing . . .</b>")
    if message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP, ChatType.PRIVATE):
        gagal = await EMO.GAGAL(client)
        alasan = await EMO.ALASAN(client)
        chat_id = message.chat.id
        blacklist = await get_chat(client.me.id)
        if chat_id in blacklist:
            return await Tm.edit(f"<b>{gagal} Group:</b> <blockquote>{message.chat.title}</blockquote>\n{alasan} <b>Ket:</b> <blockquote>Gagal Masuk Daftar Blacklist</blockquote>")
        gagal = await EMO.GAGAL(client)
        sukses = await EMO.SUKSES(client)
        alasan = await EMO.ALASAN(client)
        add_blacklist = await add_chat(client.me.id, chat_id)
        if add_blacklist:
            return await Tm.edit(f"<b>{sukses} Group:</b> <blockquote>{message.chat.title}</blockquote>\n<b>{alasan} Ket:</b> <blockquote>Berhasil Dimasukan Ke Daftar Blacklist</blockquote>")
        else:
            return await Tm.edit(f"<b><i>{gagal} ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ</i><b>")
    else:
        return await Tm.edit(f"<blockquote>{gagal} Kontol Tau Konsep Addbl Ga Sih, Cuman Buat Grup</blockquote>")


async def del_blacklist(client, message):
    proses = await EMO.PROSES(client)
    Tm = await message.reply(f"<b>{proses} Sabar Jing . . .</b>")
    if message.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP):
        try:
            if not get_arg(message):
                chat_id = message.chat.id
            else:
                chat_id = int(message.command[1])
            gagal = await EMO.GAGAL(client)
            blacklist = await get_chat(client.me.id)
            if chat_id not in blacklist:
                return await Tm.edit(f"{message.chat.title} {gagal} <blockquote>Group Ini Tidak Ada Di Daftar Blacklist</blockquote>")
            gagal = await EMO.GAGAL(client)
            sukses = await EMO.SUKSES(client)
            del_blacklist = await remove_chat(client.me.id, chat_id)
            if del_blacklist:
                return await Tm.edit(f"{sukses} {chat_id} <pre>Group Ini Berhasil Di Hapus Dari Daftar Blacklist</pre>")
            else:
                return await Tm.edit(f"{gagal} <b>Terjadi Kesalahan Yang Tidak Diketahui</b>")
        except Exception as error:
            return await Tm.edit(error)
    else:
        return await Tm.edit(f"{gagal} <b>Modul Khusus Di Group Doang Jink</b>")


async def get_blacklist(client, message):
    proses = await EMO.PROSES(client)
    Tm = await message.reply(f"<b>{proses} Processing. . .</b>")
    msg = f"<b>• Total Blacklist {len(await get_chat(client.me.id))}</b>\n\n"
    for X in await get_chat(client.me.id):
        try:
            get = await client.get_chat(X)
            msg += f"<b>• {get.title} | <code>{get.id}</code></b>\n"
        except:
            msg += f"<b>• <code>{X}</code></b>\n"
    await Tm.delete()
    await message.reply(msg)


async def rem_all_blacklist(client, message):
    proses = await EMO.PROSES(client)
    msg = await message.reply(f"{proses} <b>Processing...</b>", quote=True)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.SUKSES(client)
    get_bls = await get_chat(client.me.id)
    if len(get_bls) == 0:
        return await msg.edit(f"<b>{gagal} Daftar Blacklist Kosong</b>")
    for X in get_bls:
        await remove_chat(client.me.id, X)
    await msg.edit(f"<b>{sukses} Semua Daftar Blacklist Berhasil Dihapus</b>")


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 ℝ𝔼𝕊𝔼𝕃𝕃𝔼ℝ #
# ========================== #


async def seles_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<b>ᴛᴜɴɢɢᴜ sᴇʙᴇɴᴛᴀʀ . . .</b>")
    if not user_id:
        return await Tm.edit("<blockquote>Balas Pesan Pengguna Atau Berikan User Id/Username</blockquote>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    reseller = await get_seles()
    if user.id in reseller:
        return await Tm.edit("<pre>Sudah Jadi Reseller</pre>.")
    added = await add_seles(user.id)
    if added:
        await add_prem(user.id)
        await Tm.edit(f"<blockquote>✅ {user.mention} Telah Menjadi Reseller</blockquote>")
    else:
        await Tm.delete()
        await message.reply_text("ᴛᴇʀᴊᴀᴅɪ ᴋᴇsᴀʟᴀʜᴀɴ ʏᴀɴɢ ᴛɪᴅᴀᴋ ᴅɪᴋᴇᴛᴀʜᴜɪ")


async def unseles_user(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<b>Tunggu Sebentar . . .</b>")
    if not user_id:
        return await Tm.edit("<b>Balas Pesan Pengguna Atau Berikan User Id/Username</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        await Tm.edit(error)
    delreseller = await get_seles()
    if user.id not in delreseller:
        return await Tm.edit("Tidak Di Temukan")
    removed = await remove_seles(user.id)
    if removed:
        await remove_prem(user.id)
        await Tm.edit(f"{user.mention} Berhasil Di Hapus")
    else:
        await Tm.delete()
        await message.reply_text("Terjadi Kesalahan Yang Tidak Di Ketahui")


async def get_seles_user(cliebt, message):
    text = ""
    count = 0
    for user_id in await get_seles():
        try:
            user = await bot.get_users(user_id)
            count += 1
            user = f"• {count}: <a href=tg://user?id={user.id}>{user.first_name} {user.last_name or ''}</a> > <code>{user.id}</code>"
        except Exception:
            continue
        text += f"{user}\n"
    if not text:
        await message.reply_text("Tidak Ada Pengguna Yang Di Temukan")
    else:
        await message.reply_text(text)


# ========================== #
# 𝔻𝔸𝕋𝔸𝔹𝔸𝕊𝔼 𝔼𝕏ℙ𝕀ℝ𝔼𝔻 #
# ========================== #


async def expired_add(client, message):
    Tm = await message.reply("<blockquote><b>Processing . . .</b></blockquote>")
    user_id, get_day = await extract_user_and_reason(message)
    if not user_id:
        return await Tm.edit(f"<b>{message.text} User Id/Username - Hari</b>")
    elif user_id not in ubot._get_my_id:
        return await Tm.edit(f"<b>{user_id} Tidak Ada Dalam System</b>")
    try:
        get_id = (await client.get_users(user_id)).id
    except Exception as error:
        return await Tm.edit(error)
    if not get_day:
        get_day = 30
    now = datetime.now(timezone("Asia/Jakarta"))
    expire_date = now + timedelta(days=int(get_day))
    await set_expired_date(user_id, expire_date)
    await Tm.edit(f"<blockquote><b>{get_id} Telah Di Aktifkan Selama {get_day} Hari.</b></blockquote>")


async def expired_cek(client, message):
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply("Pengguna Tidak Di Temukan")
    expired_date = await get_expired_date(user_id)
    if expired_date is None:
        await message.reply(f"{user_id} Belum Di Aktifkan.")
    else:
        remaining_days = (expired_date - datetime.now()).days
        await message.reply(f"<blockquote><b>{user_id} Aktif Hingga {expired_date.strftime('%d-%m-%Y %H:%M:%S')}. Sisa Waktu Aktif {remaining_days} Hari.</b></blockquote>")


async def un_expired(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("</b>Processing. . .</b>")
    if not user_id:
        return await Tm.edit("<b>User Tidak Di Temukan</b>")
    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await Tm.edit(error)
    await rem_expired_date(user.id)
    return await Tm.edit(f"<b>✅ {user.id} Expired Telah Dihapus</b>")
