import asyncio
import os

from pyrogram import emoji
from pyrogram.errors import StickersetInvalid, YouBlockedUser
from pyrogram.raw.functions.messages import DeleteHistory, GetStickerSet
from pyrogram.raw.types import InputStickerSetShortName

from PyroUbot import *


async def kang_cmd(client, message):
    replied = message.reply_to_message
    msg_text = await message.reply(f"<blockquote>Boleh Juga Ni Sticker nya Maling Aahhh...</blockquote>")
    media_ = None
    emoji_ = None
    is_anim = False
    is_video = False
    resize = False
    ff_vid = False
    if replied and replied.media:
        if replied.photo:
            resize = True
        elif replied.document and "image" in replied.document.mime_type:
            resize = True
            replied.document.file_name
        elif replied.document and "tgsticker" in replied.document.mime_type:
            is_anim = True
            replied.document.file_name
        elif replied.document and "video" in replied.document.mime_type:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.animation:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.video:
            resize = True
            is_video = True
            ff_vid = True
        elif replied.sticker:
            if not replied.sticker.file_name:
                await msg_text.edit("<b>Sticker Tidak Memiliki Nama</b>")
                return
            emoji_ = replied.sticker.emoji
            is_anim = replied.sticker.is_animated
            is_video = replied.sticker.is_video
            if not (replied.sticker.file_name.endswith(".tgs") or replied.sticker.file_name.endswith(".webm")):
                resize = True
                ff_vid = True
        else:
            await msg_text.edit("<b>ғɪʟᴇ ᴛɪᴅᴀᴋ ᴅɪᴅᴜᴋᴜɴɢ</b>")
            return
        media_ = await client.download_media(replied)
    else:
        await msg_text.edit("<blockquote>Silahkan Reply Ke Media/Gif/Sticker!</blockquote>")
        return
    if media_:
        args = get_arg(message)
        pack = 1
        if len(args) == 2:
            emoji_, pack = args
        elif len(args) == 1:
            if args[0].isnumeric():
                pack = int(args[0])
            else:
                emoji_ = args[0]

        if emoji_ and emoji_ not in (getattr(emoji, _) for _ in dir(emoji) if not _.startswith("_")):
            emoji_ = None
        if not emoji_:
            emoji_ = "✨"

        u_name = f"{message.from_user.first_name} {message.from_user.last_name or ''}"
        packname = f"stkr_{str(message.from_user.id)}_by_{bot.me.username}"
        custom_packnick = f"{u_name} ꜱᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ"
        packnick = f"{Fonts.smallcap(f'{custom_packnick} ᴠᴏʟ.{pack}')}"
        cmd = "/newpack"
        if resize:
            try:
                media_ = await resize_media(media_, is_video, ff_vid)
            except Exception as error:
                return await msg_text.edit(str(error))
        if is_anim:
            packname += "_animated"
            packnick += " (ᴀɴɪᴍᴀᴛᴇᴅ)"
            cmd = "/newanimated"
        if is_video:
            packname += "_video"
            packnick += " (ᴠɪᴅᴇᴏ)"
            cmd = "/newvideo"
        exist = False
        while True:
            try:
                exist = await client.invoke(GetStickerSet(stickerset=InputStickerSetShortName(short_name=packname), hash=0))
            except StickersetInvalid:
                exist = False
                break
            limit = 50 if (is_video or is_anim) else 120
            if exist.set.count >= limit:
                pack += 1
                packname = f"stkr_{str(message.from_user.id)}_by_{bot.me.username}"
                packnick = f"{Fonts.smallcapc(f'{custom_packnick} ᴠᴏʟ.{pack}')}"
                if is_anim:
                    packname += f"_anim{pack}"
                    packnick += f" (ᴀɴɪᴍᴀᴛᴇᴅ){pack}"
                if is_video:
                    packname += f"_video{pack}"
                    packnick += f" (ᴠɪᴅᴇᴏ){pack}"
                await msg_text.edit(f"<code>ᴍᴇᴍʙᴜᴀᴛ ꜱᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ʙᴀʀᴜ {pack} ᴋᴀʀᴇɴᴀ ꜱᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ꜱᴜᴅᴀʜ ᴘᴇɴᴜʜ</code>")
                continue
            break
        if exist is not False:
            try:
                await client.send_message("stickers", "/addsticker")
            except YouBlockedUser:
                await client.unblock_user("stickers")
                await client.send_message("stickers", "/addsticker")
            except Exception as e:
                return await msg_text.edit(f"<b>ERROR:</b> <code>{e}</code>")
            await asyncio.sleep(2)
            await client.send_message("stickers", packname)
            await asyncio.sleep(2)
            limit = "50" if is_anim else "120"
            while limit in await get_response(message, client):
                await get_vars(client.me.id, "KANG_PACK") or "5280786999102415056"
                pack += 1
                packname = f"stkr_{str(message.from_user.id)}_by_{bot.me.username}"
                packnick = f"{Fonts.smallcapc(f'{ustom_packnick} ᴠᴏʟ.{pack}')}"
                if is_anim:
                    packname += "_anim"
                    packnick += " (ᴀɴɪᴍᴀᴛᴇᴅ)"
                if is_video:
                    packname += "_video"
                    packnick += " (ᴠɪᴅᴇᴏ)"
                await msg_text.edit(f"<code>ᴍᴇᴍʙᴜᴀᴛ ꜱᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ʙᴀʀᴜ {pack} ᴋᴀʀᴇɴᴀ ꜱᴛɪᴄᴋᴇʀ ᴘᴀᴄᴋ ꜱᴜᴅᴀʜ ᴘᴇɴᴜʜ</code>")
                await client.send_message("stickers", packname)
                await asyncio.sleep(2)
                if await get_response(message, client) == "Invalid pack selected.":
                    await client.send_message("stickers", cmd)
                    await asyncio.sleep(2)
                    await client.send_message("stickers", packnick)
                    await asyncio.sleep(2)
                    await client.send_document("stickers", media_)
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", emoji_)
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", "/publish")
                    await asyncio.sleep(2)
                    if is_anim:
                        await client.send_message(
                            "Stickers",
                            f"<code>{packnick}</code>",
                        )
                        await asyncio.sleep(2)
                    await client.send_message("Stickers", "/skip")
                    await asyncio.sleep(2)
                    await client.send_message("Stickers", packname)
                    await asyncio.sleep(2)
                    await msg_text.edit(f"<blockquote><b>Sticker Berhasil Di Tambahkan</b>\n          <b>[Crot Ah](https://t.me/addstickers/{packname})</b> \n<b>Untuk Menamnahkan Sticker</b></blockquote>")
                    await asyncio.sleep(2)
                    user_info = await client.resolve_peer("@Stickers")
                    return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))
            await client.send_document("stickers", media_)
            await asyncio.sleep(2)
            if await get_response(message, client) == "Sorry, the file type is invalid.":
                await msg_text.edit("<b>ɢᴀɢᴀʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ꜱᴛɪᴄᴋᴇʀ, ɢᴜɴᴀᴋᴀɴ @Stickers Bot ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ꜱᴛɪᴄᴋᴇʀ ᴀɴᴅᴀ.</b>")
                return
            await client.send_message("Stickers", emoji_)
            await asyncio.sleep(2)
            await client.send_message("Stickers", "/done")
        else:
            await msg_text.edit("<blockquote>Membuat Sticker Pack Baru</blockquote>")
            try:
                await client.send_message("Stickers", cmd)
            except YouBlockedUser:
                await client.unblock_user("stickers")
                await client.send_message("stickers", "/addsticker")
            await asyncio.sleep(2)
            await client.send_message("Stickers", packnick)
            await asyncio.sleep(2)
            await client.send_document("stickers", media_)
            await asyncio.sleep(2)
            if await get_response(message, client) == "Sorry, the file type is invalid.":
                await msg_text.edit("<b>ɢᴀɢᴀʟ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ꜱᴛɪᴄᴋᴇʀ, ɢᴜɴᴀᴋᴀɴ @Stickers Bot ᴜɴᴛᴜᴋ ᴍᴇɴᴀᴍʙᴀʜᴋᴀɴ ꜱᴛɪᴄᴋᴇʀ ᴀɴᴅᴀ.</b>")
                return
            await client.send_message("Stickers", emoji_)
            await asyncio.sleep(2)
            await client.send_message("Stickers", "/publish")
            await asyncio.sleep(2)
            if is_anim:
                await client.send_message("Stickers", f"<code>{packnick}</code>")
                await asyncio.sleep(2)
            await client.send_message("Stickers", "/skip")
            await asyncio.sleep(2)
            await client.send_message("Stickers", packname)
            await asyncio.sleep(2)
        await msg_text.edit(f"<blockquote><b>Sticker Berhasil Di Tambahkan</b>\n          <b>[Croott Ahh](https://t.me/addstickers/{packname})</b> \n<b>Untuk Menambahkan Stickee</b></blockquote>")
        await asyncio.sleep(2)
        if os.path.exists(str(media_)):
            os.remove(media_)
        user_info = await client.resolve_peer("@Stickers")
        return await client.invoke(DeleteHistory(peer=user_info, max_id=0, revoke=True))


async def get_response(message, client):
    return [x async for x in client.get_chat_history("Stickers", limit=1)][0].text
