from platform import python_version
from pyrogram import __version__
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup

from PyroUbot import LOGS_MAKER_UBOT, OWNER_ID, bot, get_expired_date, ubot
from PyroUbot.core.function.plugins import HELP_COMMANDS



class MSG:
    async def STATUS_UB(id):
        user = [x for x in ubot._ubot if x.me.id == int(id)]
        prefix = await ubot.get_prefix(id)
        if user:
            for x in user:
                expired_date = await get_expired_date(x.me.id)
                text = f"""
<pre/>{bot.me.mention}
    Nama User : [{x.me.first_name} {x.me.last_name}](tg://user?id={x.me.id})
    Status Ubot : ✅ Aktif
    Masa Aktif Ubot : {expired_date.strftime('%d-%m-%Y')} 
    Prefixes : {' '.join(prefix)}
    Status User : Babunya Butterfly</pre>
"""
        else:
            me = await bot.get_users(int(id))
            text = f"""
{bot.me.mention}
    Nama User : [{me.first_name} {me.last_name}](tg://user?id={me.id})
    Status Ubot : ❎ Tidak Aktif
    Masa Aktif Ubot : Belum Di Aktifkan
    Prefixes : {' '.join(prefix)}
    Status User : Bukan Babunya Butterfly            
"""
        return text

    def EXPIRED_MSG_BOT(X):
        return f"""
<b>❏ Pemberitahuan</b>
<b>├ Akun:</b> <a href=tg://user?id={X.me.id}>{X.me.first_name} {X.me.last_name or ''}</a>
<b>├ Id:</b> <code>{X.me.id}</code>
<b>╰ Masa Aktif Telah Habis</b>
"""

    def START(message):
        if not message.from_user.id == OWNER_ID:
            msg = f"""
<blockquote><b>Modules: {len(HELP_COMMANDS)}
Python : {python_version()}
Pyrogram : {__version__}
User: {len(ubot._ubot)}

👋🏻 Halo <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>!! {bot.me.mention} Adalah Bot Yang Dibuat Untuk Membuat Userbot Dengan Mudah. Apa Ada Yang Bisa Saya Bantu? Jika Kamu Sudah Melakukan Pembayaran Silahkan Klik Tombol Buat Userbot.</b></blockquote>
"""
        else:
            msg = f"""
<blockquote><b>Mode Owner Bot: <a href=tg://user?id={message.from_user.id}>{message.from_user.first_name} {message.from_user.last_name or ''}</a>

Gunakan Tombol Di Bawah Dengan Pinter Ya Tol</b></blockquote>
"""
        return msg

    def TEXT_PAYMENT(harga, total, bulan):
        return f"""
<blockquote><b>💬 Silahkan Melakukan Pembayaran Terlebih Dahulu

🎟️ Harga Perbulan: {harga}.000

💳 Metode Pembayaran:</b>
├──• Dana 
├─• <code>081366697938</code>
└──• <a href=https://link.dana.id/qr/47pj0yv>Klik Kontol</a>

🔖 Total Harga: Rp {total}.000
🗓️ Total Bulan: {bulan}

✅ Klik Tombol Ini Untuk Anda Mengirimkan Bukti Pembayaran</b></blockquote>
"""

    def POLICY():
        return """
<blockquote><b>↪️ Kebijakan Pengembalian

Setelah melakukan pembayaran, jika Anda belum memperoleh/
menerima manfaat dari pembelian,
Anda dapat menggunakan hak penggantian dalam waktu 2 hari setelah pembelian. Namun, jika
Anda telah menggunakan/menerima salah satu manfaat dari
pembelian, termasuk akses ke fitur pembuatan userbot, maka
Anda tidak lagi berhak atas pengembalian dana.

🆘 Dukungan
Untuk mendapatkan dukungan, Anda dapat:
• Menghubungi admin dibawah ini
• Support @Forsupportxbutterfly di Telegram
⚠️ JANGAN menghubungi Dukungan Telegram atau Dukungan Bot untuk meminta dukungan terkait pembayaran yang dilakukan di bot ini.
👉🏻 Tekan tombol Lanjutkan untuk menyatakan bahwa Anda telah
membaca dan menerima ketentuan ini dan melanjutkan
pembelian. Jika tidak, tekan tombol Batalkan</b></blockquote>
"""

    async def USERBOT(count):
        expired_date = await get_expired_date(ubot._ubot[int(count)].me.id)
        return f"""
<b>❏ Userbot Ke</b> <code>{int(count) + 1}/{len(ubot._ubot)}</code>
<b> ├ Akun:</b> <a href=tg://user?id={ubot._ubot[int(count)].me.id}>{ubot._ubot[int(count)].me.first_name} {ubot._ubot[int(count)].me.last_name or ''}</a> 
<b> ├ Id:</b> <code>{ubot._ubot[int(count)].me.id}</code>
<b> ╰ Expired</b> <code>{expired_date.strftime('%d-%m-%Y')}</code>
"""


async def sending_user(user_id):
    try:
        await bot.send_message(
            user_id,
            "Silahkan Buat Kembali Userbot Anda",
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Buat Userbot",
                            callback_data="bahan",
                        )
                    ],
                ]
            ),
            disable_web_page_preview=True,
        )
    except:
        await bot.send_message(
            LOGS_MAKER_UBOT,
            f"""
➡️ Yanh Merasa Memiliki Id: {user_id}

✅ Silahkan Buat Ulang Userbot Di: @{bot.me.username}
    """,
            reply_markup=InlineKeyboardMarkup(
                [
                    [
                        InlineKeyboardButton(
                            "Cek Masa Aktif",
                            callback_data=f"cek_masa_aktif {user_id}",
                        )
                    ],
                ]
            ),
            disable_web_page_preview=True,
        )