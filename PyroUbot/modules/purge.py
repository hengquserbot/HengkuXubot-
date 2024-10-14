from PyroUbot import *

__MODULE__ = "Purge"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Purge</b></blockquote>

<blockquote><b>๏ Perintah: {0}purge [Reply Pesan]
◉ Penjelasan: Menghapus Semua Pesan Dari Yang Di Reply</b></blockquote>
<blockquote><b>๏ Perintah: {0}del [Reply Pesan]
◉ Penjelasan: Hapus Pesan Yang Di Reply</b></blockquote>
<blockquote><b>๏ Perintah: {0}purgeme [Number Of Messages]
◉ Penjelasan: Hapus Pesan Anda Sendiri Dengan Jumlh Yang Di Tentukan</b></blockquote>
"""


@PY.UBOT("del")
@PY.TOP_CMD
async def _(client, message):
    await del_cmd(client, message)


@PY.UBOT("purgeme")
@PY.TOP_CMD
async def _(client, message):
    await purgeme_cmd(client, message)


@PY.UBOT("purge")
@PY.TOP_CMD
async def _(client, message):
    await purge_cmd(client, message)
