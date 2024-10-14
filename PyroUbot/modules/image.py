from PyroUbot import *

__MODULE__ = "Image"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Image</b></blockquote>

<blockquote><b>๏ Perintah: {0}rbg [Reply Photo]
◉ Penjelasan: Untuk Menghapus Latar Belakang Gambar</b></blockquote>
<blockquote><b>๏ Perintah: {0}blur [Reply Photo]
◉ Penjelasan: Untuk Memberikan Efek Blur Ke Gambar</b></blockquote>
<blockquote><b>๏ Perintah: {0}miror [Reply Photo]
◉ Penjelasan: Untuk Memberikan Efek Cermin Ke Gambar</b></blockquote>
<blockquote><b>๏ Perintah: {0}negative [Reply Photo]
◉ Penjelasan: Untuk Memberikan Efek Negative Ke Gambar</b></blockquote>
"""


@PY.UBOT("rbg")
@PY.TOP_CMD
async def _(client, message):
    await rbg_cmd(client, message)


@PY.UBOT("blur")
@PY.TOP_CMD
async def _(client, message):
    await blur_cmd(client, message)


@PY.UBOT("negative")
@PY.TOP_CMD
async def _(client, message):
    await negative_cmd(client, message)


@PY.UBOT("miror")
@PY.TOP_CMD
async def _(client, message):
    await miror_cmd(client, message)
