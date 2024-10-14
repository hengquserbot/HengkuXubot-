from PyroUbot import *

__MODULE__ = "Read"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Read</b></blockquote>

<blockquote><b>๏ Perintah: {0}ocr [Reply Media]
◉ Penjelasan: Untuk Membaca Text Pada Media</b></blockquote>
"""


@PY.UBOT("ocr")
@PY.TOP_CMD
async def _(client, message):
    await read_cmd(client, message)
