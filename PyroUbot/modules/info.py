from asyncio import gather
from os import remove

from pyrogram.enums import ChatType

from PyroUbot import *

__MODULE__ = "Info"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Info</b></blockquote>

<blockquote><b>๏ Perintah: {0}info [User Id/Username/Reply To User]
◉ Penjelasan: Untuk Mendapatkan Info Detail Dari User</b></blockquote>
<blockquote><b>๏ Perintah: {0}cinfo [Chat Id/Username/Reply To Chat]
◉ Penjelasan: Untuk Mendapatkan Info Detail Dari Grup/Channel</b></blockquote>
<blockquote><b>๏ Perintah: {0}id
◉ Penjelasan: Untuk Cek Id User/Grup/Channel</b></blockquote>
<blockquote><b>๏ Perintah: {0}id [Reply User/Media]
◉ Penjelasan: Untuk Mengetahui Id Dari User/Media</b></blockquote>
<blockquote><b>๏ Perintah: {0}id [Username User/Grup/Channel]
◉ Penjelasan: Untuk Cek Id User/Grup/Channel Melalui Username</b></blockquote>
"""




@PY.UBOT("info")
@PY.TOP_CMD
async def info_cmd(client, message):
    user_id = await extract_user(message)
    Tm = await message.reply("<blockquote><b>Processing . . .</b></blockquote>")
    if not user_id:
        return await Tm.edit("<blockquote><b>Berikan Userid/Username/Reply Untuk Mendapatkan Info Pengguna Tersebut.</b></blockquote>")
    try:
        user = await client.get_users(user_id)
        username = f"@{user.username}" if user.username else "-"
        first_name = f"{user.first_name}" if user.first_name else "-"
        last_name = f"{user.last_name}" if user.last_name else "-"
        fullname = f"{user.first_name} {user.last_name}" if user.last_name else user.first_name
        user_details = (await client.get_chat(user.id)).bio
        bio = f"{user_details}" if user_details else "-"
        h = f"{user.status}"
        if h.startswith("UserStatus"):
            y = h.replace("UserStatus.", "")
            status = y.capitalize()
        else:
            status = "-"
        dc_id = f"{user.dc_id}" if user.dc_id else "-"
        common = await client.get_common_chats(user.id)
        out_str = f"""
<blockquote><b>User Information:

🆔 User Id: {user.id}
👤 First Name: {first_name}
🗣️ Last Name: {last_name}
🌐 Username: {username}
🏛️ Dc Id: {dc_id}
🤖 Is Bot: {user.is_bot}
🚷 Is Scam: {user.is_scam}
🚫 Restricted: {user.is_restricted}
✅ Verified: {user.is_verified}
⭐ Premium: {user.is_premium}
📝 User Bio: {bio}

👀 Same Groups Seen: {len(common)}
👁️ Last Seen: {status}
🔗 User Permanent Link: <a href=tg://user?id={user.id}>{fullname}</a></b></blockquote>
"""
        photo_id = user.photo.big_file_id if user.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                Tm.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=message.id,
                ),
            )
            remove(photo)
        else:
            await Tm.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await Tm.edit(f"Info: {e}")



@PY.UBOT("cinfo")
@PY.TOP_CMD
async def cinfo_cmd(client, message):
    Tm = await message.reply("<blockquote><b>Processing . . .</b></blockquote>")
    try:
        if len(message.text.split()) > 1:
            chat_u = message.text.split()[1]
            chat = await client.get_chat(chat_u)
        else:
            if message.chat.type == ChatType.PRIVATE:
                return await Tm.edit(f"<blockquote><b>Gunakan Perintah Ini Di Dalam Grup Atau Gunakan {PREFIX[0]}cinfo [Group Username Atau Id]</b></blockquote>")
            else:
                chatid = message.chat.id
                chat = await client.get_chat(chatid)
        h = f"{chat.type}"
        if h.startswith("ChatType"):
            y = h.replace("ChatType.", "")
            type = y.capitalize()
        else:
            type = "Private"
        username = f"@{chat.username}" if chat.username else "-"
        description = f"{chat.description}" if chat.description else "-"
        dc_id = f"{chat.dc_id}" if chat.dc_id else "-"
        out_str = f"""
<blockquote><b>Chat Information:

🆔 Chat Id: <code>{chat.id}</code>
👥 Title: {chat.title}
👥 Username: {username}
📩 Type: <code>{type}</code>
🏛️ Dc Id: <code>{dc_id}</code>
🗣️ Is Scam: <code>{chat.is_scam}</code>
🎭 Is Fake: <code>{chat.is_fake}</code>
✅ Verified: <code>{chat.is_verified}</code>
🚫 Restricted: <code>{chat.is_restricted}</code>
🔰 Protected: <code>{chat.has_protected_content}</code>

🚻 Total Members: <code>{chat.members_count}</code>
📝 Description: <code>{description}</code></b></blockquote>
"""
        photo_id = chat.photo.big_file_id if chat.photo else None
        if photo_id:
            photo = await client.download_media(photo_id)
            await gather(
                Tm.delete(),
                client.send_photo(
                    message.chat.id,
                    photo,
                    caption=out_str,
                    reply_to_message_id=message.id,
                ),
            )
            remove(photo)
        else:
            await Tm.edit(out_str, disable_web_page_preview=True)
    except Exception as e:
        return await Tm.edit(f"Info: `{e}`")
