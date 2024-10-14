from PyroUbot import *

__MODULE__ = "Copy"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Copy</b></blockquote>

<blockquote><b>๏ Perintah: <code>{0}copy</code> [Link Konten Telegram]
◉ Penjelasan: Untuk Mengambil Pesan Telegram Melalui Link</b></blockquote>
<blockquote><b>๏ Perintah: <code>{0}thumb</code> [Reoly Video + Link Teleghraph] 
◉ Penjelasan: Untuk Merubah Thumbnail / Profil Awal Video, Dengan Gambar Yang Di Inginkan</b></blockquote>
<blockquote><b>✘ Contoh Penggunaan:
  Reply Video Yang Ingin Di Ubah Thumbnailnya, Lalu Ketik Perintah <code>{0}thumb</code> https://telegra.ph//file/21[Link Teleghraph]</b></blockquote>
  """


@PY.BOT("copy")
async def _(client, message):
    await copy_bot_msg(client, message)


@PY.UBOT("copy")
@PY.TOP_CMD
async def _(client, message):
    await copy_ubot_msg(client, message)


@PY.INLINE("^get_msg")
@INLINE.QUERY
async def _(client, inline_query):
    await copy_inline_msg(client, inline_query)


@PY.CALLBACK("^copymsg")
@INLINE.DATA
async def _(client, callback_query):
    await copy_callback_msg(client, callback_query)
