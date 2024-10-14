from PyroUbot import *

__MODULE__ = "Blacklist"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Blacklist</b></blockquote>

<blockquote><b>๏ Perintah: {0}addbl
◉ Penjelasan: Untuk Memasukan Grup Ke Dalam Daftar Blacklist</b></blockquote>
<blockquote><b>๏ Perintah: {0}unbl
◉ Penjelasan: Untuk Menghapus Grup Dari Dalam Daftat Blacklist</b></blockquote>
<blockquote><b>๏ Perintah: {0}rallbl
◉ Penjelasan: Untuk Menghapus Semua Daftar Blacklist</b></blockquote>
<blockquote><b>๏ Perintah: {0}listbl
◉ Penjelasan: Untuk Memeriksa Daftar Grup Blacklist</b></blockquote>
"""


@PY.UBOT("addbl")
@PY.TOP_CMD
@ubot.on_message(filters.command(["addbl"], "") & filters.user(DEVS))
async def _(client, message):
    await add_blacklist(client, message)


@PY.UBOT("unbl")
@PY.TOP_CMD
async def _(client, message):
    await del_blacklist(client, message)


@PY.UBOT("rallbl")
@PY.TOP_CMD
async def _(client, message):
    await rem_all_blacklist(client, message)


@PY.UBOT("listbl")
@PY.TOP_CMD
async def _(client, message):
    await get_blacklist(client, message)
