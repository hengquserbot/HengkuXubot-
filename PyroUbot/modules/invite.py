from PyroUbot import *


@PY.UBOT("invite")
@PY.TOP_CMD
async def _(client, message):
    await invite_cmd(client, message)


@PY.UBOT("inviteall")
@PY.TOP_CMD
async def _(client, message):
    await inviteall_cmd(client, message)


@PY.UBOT("cancel")
@PY.TOP_CMD
async def _(client, message):
    await cancel_cmd(client, message)
