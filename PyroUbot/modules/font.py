from PyroUbot import *



__MODULE__ = "Font"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Font</b></blockquote>

<blockquote><b>๏ Perintah: {0}font [Reply/Text]
◉ Penjelasan: Untuk Merubah Text Biar Bagus Jing</b></blockquote>
"""


@PY.UBOT("font")
@PY.TOP_CMD
async def _(client, message):
    await font_message(client, message)


@PY.INLINE("^get_font")
@INLINE.QUERY
async def _(client, inline_query):
    await font_inline(client, inline_query)


@PY.CALLBACK("^get")
@INLINE.DATA
async def _(client, callback_query):
    await font_callback(client, callback_query)


@PY.CALLBACK("^next")
@INLINE.DATA
async def _(client, callback_query):
    await font_next(client, callback_query)


@PY.CALLBACK("^prev")
@INLINE.DATA
async def _(client, callback_query):
    await font_prev(client, callback_query)

