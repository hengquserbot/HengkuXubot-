from PyroUbot import *

__MODULE__ = "Emoji"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Emoji</b></blockquote>

<blockquote><b>๏ Perintah: {0}setemoji - [Kata Kunci] [Emoji Prem]
  Kata Kunci:
  PING1
  PING2
  PING3
  PROSES
  GAGAL
  SUKSES
  ◉ Penjelasan: Untuk Ngubah Tampilan Emoji Buat Yang Premium</b></blockquote>
"""


@PY.UBOT("setemoji")
@PY.TOP_CMD
async def _(client, message):
    await change_emot(client, message)
