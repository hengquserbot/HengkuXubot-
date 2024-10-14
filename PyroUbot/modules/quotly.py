from PyroUbot import *

__MODULE__ = "Quotly"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Quotly</b></blockquote>

<blockquote><b>๏ Perintah: {0}q [Reply Text]
◉ Penjelasan: Untuk Merubah Text Jadi Sticker</b></blockquote>
"""


@PY.UBOT("q")
@PY.TOP_CMD
async def _(client, message):
    await quotly_cmd(client, message)
