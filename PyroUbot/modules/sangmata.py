from PyroUbot import *

__MODULE__ = "Sangmata"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Sangmata</b></blockquote>

<blockquote><b>๏ Perintah: {0}sg [User Id/Username]
◉ Penjelasan: Untuk Lu Yang Suka Kepo</b></blockquote>
"""


@PY.UBOT("sg")
@PY.TOP_CMD
async def _(client, message):
    await sg_cmd(client, message)
