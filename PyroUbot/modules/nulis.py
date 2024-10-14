from PyroUbot import *


@PY.UBOT("nulis")
@PY.TOP_CMD
async def _(client, message):
    await nulis_cmd(client, message)
