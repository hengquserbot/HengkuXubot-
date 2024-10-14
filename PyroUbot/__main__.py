import asyncio

from pyrogram import idle
from PyroUbot import *


async def main():
    await bot.start()
    for _ubot in await get_userbots():
        ubot_ = Ubot(**_ubot)
        try:
            await asyncio.wait_for(ubot_.start(), timeout=10)
            await ubot_.join_chat("Forsupportxbutterfly")
            await ubot_.join_chat("Zpranstore")
            await ubot_.join_chat("sellerjancok") 
        except asyncio.TimeoutError:
            await remove_ubot(int(_ubot["name"]))
            await rem_expired_date(int(_ubot["name"]))
            print(f"[INFO]: {int(_ubot['name'])} TIDAK DAPAT MERESPON")
        except Exception:
            await remove_ubot(int(_ubot["name"]))
            await rem_expired_date(int(_ubot["name"]))
            print(f"[INFO]: {int(_ubot['name'])} BERHASIL DI HAPUS")
    await bash("rm -rf *session*")
    await asyncio.gather(loadPlugins(), installPeer(), expiredUserbots(), idle())



if __name__ == "__main__":
    loop = asyncio.get_event_loop_policy().get_event_loop()
    loop.run_until_complete(main())