from PyroUbot import *

__MODULE__ = "Ai"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Ai

<blockquote><b>๏ Perintah: {0}ai [Query]
◉ Penjelasan: Untuk Chatgpt</b></blockquote>
<blockquote><b>๏ Perintah: {0}dalle [Query]
◉ Penjelasan: Untuk Membuat Sebuah Photo</b></blockquote>
<blockquote><b>๏ Perintah: {0}stt [Reply Voice Note]
◉ Penjelasan: Untuk Merubah Text Ke Pesan Suara</b></blockquote>
"""


@PY.UBOT("ai")
@PY.TOP_CMD
async def _(client, message):
    await ai_cmd(client, message)


@PY.UBOT("dalle")
@PY.TOP_CMD
async def _(client, message):
    await dalle_cmd(client, message)


@PY.UBOT("stt")
@PY.TOP_CMD
async def _(client, message):
    await stt_cmd(client, message)
