from PyroUbot import *

__MODULE__ = "Spam"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Spam</b></blockquote>

<blockquote><b>๏ Perintah: {0}spam [Jumlah Pesan - Text]
◉ Penjelasan: Tau Sendiri Anjing</b></blockquote>
<blockquote><b>๏ Perintah: {0}dspam< [Jumlah Pesan - Jumlah Delay Detik - Text]
◉ Penjelasan: Untuk Delay Spam</b></blockquote>
"""


@PY.UBOT("spam")
@PY.TOP_CMD
async def _(client, message):
    await spam_cmd(client, message)


@PY.UBOT("dspam")
@PY.TOP_CMD
async def _(client, message):
    await dspam_cmd(client, message)
