from PyroUbot import *

__MODULE__ = "Animasi"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Animasi</b></blockquote>

<blockquote><b>๏ Perintah:
lopyu, hm, nah
◉ Penjelasan: <u>Coba Aja Sendiri</u></b></blockquote>
<blockquote><b>๏ Perintah: 
ror, fuck, helikopter
◉ Penjelasan: <u>Coba Aja Sendiri</u></b></blockquote>
<blockquote><b>๏ Perintah:
tembak, bundir, awk, y
◉ Penjelasan: <u>Coba Aja Sendiri</u></b></blockquote>
<blockquote><b>๏ Perintah:
tank, babi, ajg, cepongbob, peace
◉ Penjelasan: <u>Cek Aja Sendiri</u></b></blockquote>
<blockquote><b>๏ Perintah:
vcs, lipkol, nakal, kocok
◉ Penjelasan: <u>Cek Aja Sendiri</u></b></blockquote>
"""

@PY.UBOT("lopyu")
@PY.TOP_CMD
async def _(client, message):
    await lopeyo(client, message)


@PY.UBOT("hm")
@PY.TOP_CMD
async def _(client, message):
    await hmmm(client, message)


@PY.UBOT("ror")
@PY.TOP_CMD
async def _(client, message):
    await ror(client, message)


@PY.UBOT("fuck")
@PY.TOP_CMD
async def _(client, message):
    await fucek(client, message)


@PY.UBOT("helikopter")
@PY.TOP_CMD
async def _(client, message):
    await helikopter(client, message)


@PY.UBOT("tembak")
@PY.TOP_CMD
async def _(client, message):
    await dornembak(client, message)


@PY.UBOT("bundir")
@PY.TOP_CMD
async def _(client, message):
    await ngebundir(client, message)


@PY.UBOT("awk")
@PY.TOP_CMD
async def _(client, message):
    await awikwok(client, message)


@PY.UBOT("y")
@PY.TOP_CMD
async def _(client, message):
    await ysaja(client, message)


@PY.UBOT("tank")
@PY.TOP_CMD
async def _(client, message):
    await tank(client, message)


@PY.UBOT("babi")
@PY.TOP_CMD
async def _(client, message):
    await babi(client, message)


@PY.UBOT("vcs")
@PY.TOP_CMD
async def _(client, message):
    await piciieess(client, message)


@PY.UBOT("lipkol")
@PY.TOP_CMD
async def _(client, message):
    await lipkoll(client, message)


@PY.UBOT("nakal")
@PY.TOP_CMD
async def _(client, message):
    await nakall(client, message)


@PY.UBOT("peace")
@PY.TOP_CMD
async def _(client, message):
    await peace(client, message)


@PY.UBOT("cepongbob")
@PY.TOP_CMD
async def _(client, message):
    await spongebobss(client, message)


@PY.UBOT("kocok")
@PY.TOP_CMD
async def _(client, message):
    await kocokk(client, message)


@PY.UBOT("ajg")
@PY.TOP_CMD
async def _(client, message):
    await anjg(client, message)


@PY.UBOT("nah")
@PY.TOP_CMD
async def _(client, message):
    await nahlove(client, message)