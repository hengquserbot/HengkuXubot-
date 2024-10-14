from PyroUbot import *

__MODULE__ = "Memes"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Memes</b></blockquote>

<blockquote><b>๏ Perintah: {0}memes [Text]
◉ Penjelasan: Untuk Membuat Sticker Meme Random</b></blockquote>
"""


@PY.UBOT("memes")
@PY.TOP_CMD
async def _(client, message):
    await memes_cmd(client, message)
