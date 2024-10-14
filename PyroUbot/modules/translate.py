from PyroUbot import *

__MODULE__ = "Translate"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Translate</b></blockquote>

<blockquote><b>๏ Perintah: {0}tr [Reply/Text]
◉ Penjelasan: Untuk Menerjemahkan Text</b></blockquote>
<blockquote><b>๏ Perintah: {0}tts [Reply/Text]
◉ Penjelasan: Untuk Merubah Text Menjadi Pesan Suara</b></blockquote>
<blockquote><b>๏ Perintah: {0}set_lang
◉ Penjelasan: Untuk Merubah Bahasa Translate</b></blockquote>
"""


@PY.UBOT("tts")
@PY.TOP_CMD
async def _(client, message):
    await tts_cmd(client, message)


@PY.UBOT("tr")
@PY.TOP_CMD
async def _(client, message):
    await tr_cmd(client, message)


@PY.UBOT("set_lang")
@PY.TOP_CMD
async def _(client, message):
    await set_lang_cmd(client, message)


@PY.INLINE("^ubah_bahasa")
@INLINE.QUERY
async def _(client, inline_query):
    await ubah_bahasa_inline(client, inline_query)


@PY.CALLBACK("^set_bahasa")
@INLINE.DATA
async def _(client, callback_query):
    await set_bahasa_callback(client, callback_query)
