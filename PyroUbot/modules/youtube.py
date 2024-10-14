from PyroUbot import *

__MODULE__ = "Youtube"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Youtube</b></blockquote>

<blockquote><b>๏ Perintah: {0}song [Judul]
◉ Penjelasan:  Untuk Mendownload Music Yang Di Inginkan</b></blockquote>
<blockquote><b>๏ Perintah: {0}vsong [Judul]
◉ Penjelasan: Untuk Mendownload Video Yang Di Inginkan</b></blockquote>
"""


@PY.UBOT("vsong")
@PY.TOP_CMD
async def _(client, message):
    await vsong_cmd(client, message)


@PY.UBOT("song")
@PY.TOP_CMD
async def _(client, message):
    await song_cmd(client, message)
