from PyroUbot import *

__MODULE__ = "Kang"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Kang</b></blockquote>

<blockquote><b>๏ Perintah: {0}kang [Reply Media/Sticker]
◉ Penjelasan: Untuk Menambah Sticker Ke Sticker Pack.</b></blockquote>
"""


@PY.UBOT("kang")
@PY.TOP_CMD
async def _(client, message):
    await kang_cmd(client, message)
