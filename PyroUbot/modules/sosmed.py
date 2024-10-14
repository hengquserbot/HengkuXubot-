from PyroUbot import *


@PY.UBOT("sosmed")
@PY.TOP_CMD
async def _(client, message):
    await sosmed_cmd(client, message)
