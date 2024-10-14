from PyroUbot import *

__MODULE__ = "Search"
__HELP__ = """
<b>✘ Bantuan Untuk Search</b>

  <b>๏ Perintah:</b> <code>{0}pic</code> [Query]
  <b>◉ Penjelasan:</b> Untuk Mencari Foto Random Dari Google

  <b>๏ Perintah:</b> <code>{0}gif</code> [Query]
  <b>◉ Penjelasan:</b> Untuk Mencari Gift Random Dari Google
"""


@PY.UBOT("pic")
@PY.TOP_CMD
async def _(client, message):
    await pic_bing_cmd(client, message)


@PY.UBOT("bing")
@PY.TOP_CMD
async def _(client, message):
    await pic_bing_cmd(client, message)


@PY.UBOT("gif")
@PY.TOP_CMD
async def _(client, message):
    await gif_cmd(client, message)
