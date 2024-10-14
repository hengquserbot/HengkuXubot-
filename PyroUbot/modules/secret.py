from PyroUbot import *

__MODULE__ = "Secret"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Secret</b></blockquote>

<blockquote><b>๏ Perintah: {0}msg [Reply User - Text]
◉ Penjelasan: Mengirim Pesan Secara Rahasia</b></blockquote>
"""


@PY.UBOT("msg")
@PY.TOP_CMD
async def _(client, message):
    await msg_cmd(client, message)


@PY.INLINE("^secret")
@INLINE.QUERY
async def _(client, inline_query):
    await secret_inline(client, inline_query)
