from PyroUbot import *

__MODULE__ = "Qrcode"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Qrcode</b></blockquote>

<blockquote><b>๏ Perintah: {0}qrGen [Text Qrcode]
◉ Penjelasan: Untuk Merubah Qrcode Menjadi Gambar</b></blockquote>
<blockquote><b>๏ Perintah: {0}qrRead [Reply To Media]
◉ Penjelasan: Untuk Merubah Qrcode Menjadi Text</b></blockquote>
"""


@PY.UBOT("qrgen")
@PY.TOP_CMD
async def _(client, message):
    await qr_gen_cmd(client, message)


@PY.UBOT("qrread")
@PY.TOP_CMD
async def _(client, message):
    await qr_read_cmd(client, message)
