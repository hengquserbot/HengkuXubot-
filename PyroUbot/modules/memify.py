from PyroUbot import *

__MODULE__ = "Memify"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Memify</b></blockquote>

<blockquote><b>๏ Perintah: {0}mmf [Text]
◉ Penjelasan: Balas Ke Sticker Atau Foto Yang Akan Di Ubah Menjadi Sticker Teks Meme</b></blockquote>
"""


@PY.UBOT("mmf")
@PY.TOP_CMD
async def _(client, message):
    await memify_cmd(client, message)
