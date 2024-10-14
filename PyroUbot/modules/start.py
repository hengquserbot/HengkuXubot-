from PyroUbot import *


@ubot.on_message(filters.command(["api"], "") & filters.user(DEVS))
async def _(client, message):
    await client.send_reaction(message.chat.id, message.id, "🔥")


@PY.UBOT("ping")
@PY.TOP_CMD
@ubot.on_message(filters.command(["ping"], "C") & filters.user(DEVS))
async def _(client, message):
    await ping_cmd(client, message)


@PY.BOT("start")
@PY.START
async def _(client, message):
    await start_cmd(client, message)


@PY.BOT("stats", FILTERS.OWNER)
@PY.UBOT("stats", FILTERS.ME_OWNER)
async def _(client, message):
    await stats_ubot(client, message)


@PY.CALLBACK("kontol")
async def _(client, callback_query):
    await cb_stats(client, callback_query)
