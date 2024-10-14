import asyncio
from datetime import datetime

from dateutil.relativedelta import relativedelta
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from pytz import timezone

from PyroUbot import *

CONFIRM_PAYMENT = []


async def confirm_callback(client, callback_query):
    user_id = int(callback_query.from_user.id)
    full_name = f"{callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}"
    get = await bot.get_users(user_id)
    CONFIRM_PAYMENT.append(get.id)
    try:
        button = [[InlineKeyboardButton("Batalkan", callback_data=f"home {user_id}")]]
        await callback_query.message.delete()
        pesan = await bot.ask(
            user_id,
            f"<b>Silahkan Kirim Bukti Screenshot Pembayaran: {full_name}</b>",
            reply_markup=InlineKeyboardMarkup(button),
            timeout=300,
        )
    except asyncio.TimeoutError as out:
        if get.id in CONFIRM_PAYMENT:
            CONFIRM_PAYMENT.remove(get.id)
            return await bot.send_message(get.id, "ᴘᴇᴍʙᴀᴛᴀʟᴀɴ ᴏᴛᴏᴍᴀᴛɪs")
    if get.id in CONFIRM_PAYMENT:
        if not pesan.photo:
            CONFIRM_PAYMENT.remove(get.id)
            await pesan.request.edit(
                f"<b>Silahkan Kirim Bukti Screenshot Pembayaran Anda: {full_name}</b>",
            )
            buttons = [[InlineKeyboardButton("Konfirmasi", callback_data="confirm")]]
            return await bot.send_message(
                user_id,
                """
<b>Tidak Dapat Di Proses</b>

<b>Harap Kirimkan Screenshot Bukti Pembayaran Anda Yang Valid</b>

<b>Silakhakan Konfirmasi Ulang Pembayaran Anda</b>
""",
                reply_markup=InlineKeyboardMarkup(buttons),
            )
        elif pesan.photo:
            buttons = Button.button_add_expired(get.id)
            await pesan.copy(
                OWNER_ID,
                reply_markup=buttons,
            )
            CONFIRM_PAYMENT.remove(get.id)
            await pesan.request.edit(
                f"<b>Silahkan Kirim Bukti Screenshot Pembayaran Anda: {full_name}</b>",
            )
            return await bot.send_message(
                user_id,
                f"""
<b>Baik {full_name} Silahkan Di Tunggu Dan Jangan Spam Ya Jink</b>

<b>Pembayaran Anda Akan Di Konfirmasi Setelah 1-3 Jam Kerja</b>
""",
            )


async def tambah_or_kurang(client, callback_query):
    BULAN = int(callback_query.data.split()[1])
    HARGA = 30
    QUERY = callback_query.data.split()[0]
    try:
        if QUERY == "kurang":
            if BULAN > 1:
                BULAN -= 1
                TOTAL_HARGA = HARGA * BULAN
        elif QUERY == "tambah":
            if BULAN < 12:
                BULAN += 1
                TOTAL_HARGA = HARGA * BULAN
        buttons = Button.plus_minus(BULAN, callback_query.from_user.id)
        await callback_query.message.reply_text(
            MSG.TEXT_PAYMENT(HARGA, TOTAL_HARGA, BULAN),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        await callback_query.message.delete()
    except:
        pass


async def success_failed_home_callback(client, callback_query):
    query = callback_query.data.split()
    get_user = await bot.get_users(query[1])
    if query[0] == "success":
        buttons = [
            [InlineKeyboardButton("Buat Userbot", callback_data="bahan")],
        ]
        await bot.send_message(
            get_user.id,
            """
<b>Pembayaran Anda Berhasil Di Konfirmasi</b>

<b>Sekarang Anda Bisa Membuat Userbot</b>
""",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        buttons_success = [
            [InlineKeyboardButton("Dapatkan Profil", callback_data=f"profil {get_user.id}")],
        ]
        await add_prem(get_user.id)
        now = datetime.now(timezone("Asia/Jakarta"))
        expired = now + relativedelta(months=int(query[2]))
        await set_expired_date(get_user.id, expired)
        return await bot.send_message(
            OWNER_ID,
            f"""
<b>✅ {get_user.first_name} {get_user.last_name or ''} Ditambahkan Ke Anggota Premium</b>
""",
            reply_markup=InlineKeyboardMarkup(buttons_success),
        )
    if query[0] == "failed":
        buttons = [
            [InlineKeyboardButton("Lakukan Pembayaran", callback_data="bayar_dulu")],
        ]
        await bot.send_message(
            get_user.id,
            """
<b>Pembayaran Anda Tidak Dapat Di Konfirmasi</b>

<b>Silahkan Lakukan Pembayaran Dengan Benar</b>
""",
            reply_markup=InlineKeyboardMarkup(buttons),
        )
        buttons_failed = [
            [InlineKeyboardButton("Dapatkan Profil", callback_data=f"profil {get_user.id}")],
        ]
        return await bot.send_message(
            OWNER_ID,
            f"""
<b>❌ {get_user.first_name} {get_user.last_name or ''} Tidak Di Tambahkan Ke Anggota Premium</b>
""",
            reply_markup=InlineKeyboardMarkup(buttons_failed),
        )
    if query[0] == "home":
        if get_user.id in CONFIRM_PAYMENT:
            CONFIRM_PAYMENT.remove(get_user.id)
            buttons_home = Button.start(callback_query)
            await callback_query.message.delete()
            return await bot.send_message(
                get_user.id,
                MSG.START(callback_query),
                reply_markup=InlineKeyboardMarkup(buttons_home),
            )
        else:
            buttons_home = Button.start(callback_query)
            await callback_query.message.delete()
            return await bot.send_message(
                get_user.id,
                MSG.START(callback_query),
                reply_markup=InlineKeyboardMarkup(buttons_home),
            )
