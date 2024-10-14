from PyroUbot import *

__MODULE__ = "Tagall"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Tagall

<blockquote><b>๏ Perintah: {0}tagall [Reply Pesan/Text] 
◉ Penjelasan: Tau Sendiri Lah Jink</b></blockquote>
<blockquote><b>๏ Perintah: {0}stop
◉ Penjelasan: Untuk Membatalkan Tag All</b></blockquote>
"""


@PY.UBOT("tagall")
@PY.TOP_CMD
async def _(client, message):
    await tagall_cmd(client, message)


@PY.UBOT("stop")
@PY.TOP_CMD
async def _(client, message):
    await batal_cmd(client, message)
