from PyroUbot import *

__MODULE__ = "Logo"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Logo</b></blockquote>

<blockquote><b>๏ Perintah: {0}logo [Text]
◉ Penjelasan:  Untuk Membuat Sebuah Logo Dengan Background Random</b></blockquote>
<blockquote><b>๏ Perintah: {0}blogo [Text]
◉ Penjelasan: Untuk Membuat Sebuah Logo Dengan Background Hitam</b></blockquote>
"""


@PY.UBOT("logo")
@PY.TOP_CMD
async def _(client, message):
    await logo_cmd(client, message)


@PY.UBOT("blogo")
@PY.TOP_CMD
async def _(client, message):
    await logo_cmd(client, message)
