from PyroUbot import *


@PY.UBOT("id")
@PY.TOP_CMD
async def _(client, message):
    await id_cmd(client, message)
