import asyncio

from pyrogram.enums import ChatType
from pyrogram.types import ChatPermissions

from PyroUbot import *


__MODULE__ = "Admin"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Admin</b></blockquote>

<blockquote><b>๏ Perintah: {0}kick [User Id/Username/Reply User]
◉ Penjelasan: <u>Untuk Menendang Anggota Dari Grup</u></>b</blockquote>
<blockquote><b>๏ Perintah: {0}ban [User Id/Username/Reply User]
◉ Penjelasan: <u>Untuk Memblokir Anggota Dari Grup</u></b></blockquote>
<blockquote><b>๏ Perintah: {0}mute [User Id/Username/Reply User]
◉ Penjelasan: <u>Untuk Membisukan Anggota Dari Grup</u></b></blockquote>
<blockquote><b>๏ Perintah:</b> {0}unmute [User Id/Username/Reply User]
◉ Penjelasan: <u>Untuk Melepas Pembisuan Anggota Grup</u></b></blockquote>
<blockquote><b>๏ Perintah: {0}unban [User_Id/Username/Reply User]
◉ Penjelasan: <u>Untuk Melepas Ban Anggota Dari Grup</u></b></blockquote>
<blockquote><b>๏ Perintah: {0}staff
◉ Penjelasan: <u>Untuk Mengetahui Daftar Semua Admin Di Dalam Grup</u></b></blockquote>
<blockquote><b>๏ Perintah: {0}invite [Username] 
◉ Penjelasan: <u>Untuk Mengundang Anggota Ke Grup Anda</u></b></blockquote>
<blockquote><b>๏ Perintah: {0}staff [Username] 
◉ Penjelasan: <u>Cek Aja Cendili</u></b></blockquote>
"""



@PY.UBOT("kick", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_kick(client, message):
    gagal = await EMO.GAGAL(client)
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text(f"{gagal} Saya Tidak Dapat Menemukan Pengguna Itu.")
    if user_id == (await client.get_me()).id:
        return await message.reply_text(f"<blockquote><b>{gagal} Lu Gila Apa Goblok Sih Mana Bisa Nendang Diri Sendiri.</b></blockquote>")
    if user_id == OWNER_ID:
        return await message.reply_text(f"<blockquote><b>{gagal} LU TAU DIRI NGENTOD YANG BUAT LU ITU DIA SOK SOKAN MAU KICK DIA GOBLOK</b></blockquote>")
    if user_id in (await list_admins(message)):
        return await message.reply_text(f"<blockquote><b>{gagal} Orang Bego Mana Yang Mau Ngekick Admin, Goblok Lu.</b></blockquote>")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    alasan = await EMO.ALASAN(client)
    user = await EMO.USER(client)
    admin = await EMO.ADMIN(client)
    msg = f"<b>{user} Di Kick:</b> {mention}\n<b>{admin} Admin:</b> {message.from_user.mention}"
    if reason:
        msg += f"\n<b>{alasan} Alasan:</b> {reason}"
    try:
        await message.chat.ban_member(user_id)
        await message.reply(msg)
        await asyncio.sleep(1)
        await message.chat.unban_member(user_id)
    except Exception as error:
        await message.reply(error)



@PY.UBOT("ban", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_ban(client, message):
    gagal = await EMO.GAGAL(client)
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text(f"{gagal} Saya Tidak Bisa Menemukan Anggota Itu.")
    if user_id == (await client.get_me()).id:
        return await message.reply_text(f"<blockquote><b>{gagal} Lu Gila Apa Gimana Sih Mana Bisa Ban Diri Sendiri Tolol.</b></blockquote>")
    if user_id == OWNER_ID:
        return await message.reply_text(f"<blockquote><b>{gagal} ANAK TOLOL BERANI BERANINYA LO MAU BAN YANG BUAT GUA</b></blockquote>")
    if user_id in (await list_admins(message)):
        return await message.reply_text(f"<blockquote><b>{gagal} Yaa Goblok Lu Mau Nyoba Nyoba Ban Admin? Sujud Dulu Noh Di Kaki Admin.</b></blockquote>")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    alasan = await EMO.ALASAN(client)
    user = await EMO.USER(client)
    admin = await EMO.ADMIN(client)
    msg = f"<b>{user} Dibanned:</b> {mention}\n<b>{admin} Admin:</b> {message.from_user.mention}"
    if reason:
        msg += f"\n<b>{alasan} Alasan:</b> {reason}"
    try:
        await message.chat.ban_member(user_id)
        await message.reply(msg)
    except Exception as error:
        await message.reply(error)



@PY.UBOT("mute", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_mute(client, message):
    gagal = await EMO.GAGAL(client)
    user_id, reason = await extract_user_and_reason(message)
    if not user_id:
        return await message.reply_text(f"{gagal} Saya Tidak Dapat Menemukan Anggota Itu.")
    if user_id == (await client.get_me()).id:
        return await message.reply_text(f"<blockquote><b>{gagal} Tolol Mana Bisa Lu Mute Diri Sendiri Ga Percaya? Tanya Aja Pak Haji.</b></blockquote>")
    if user_id == OWNER_ID:
        return await message.reply_text(f"<blockquote><b>{gagal} Mau Mute Yang Buat Gua? Jangan Ya Dek Ya.</b></blockquote>")
    if user_id in (await list_admins(message)):
        return await message.reply_text(f"{gagal} Anak Bego Anak Bego Mana Bisa Ngemute Admin Karna Dia Admin Juga.")
    try:
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    alasan = await EMO.ALASAN(client)
    user = await EMO.USER(client)
    admin = await EMO.ADMIN(client)
    msg = f"<b>{user} Membisukan:</b> {mention}\n<b>{admin} Admin:</b> {message.from_user.mention}"
    if reason:
        msg += f"\n<b>{alasan} Alasan:</b> {reason}"
    try:
        await message.chat.restrict_member(user_id, ChatPermissions())
        await message.reply(msg)
    except Exception as error:
        await message.reply(error)



@PY.UBOT("unmute", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_unmute(client, message):
    gagal = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text(f"{gagal} Saya Tidak Menemukan Anggota Itu.")
    try:
        sukses = await EMO.SUKSES(client)
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    try:
        await message.chat.unban_member(user_id)
        await message.reply(f"<blockquote><b>{sukses} {mention} Ciee Udah Ga Di Mute Makannya Kalo Ngetik Pake Adab Ngentot Ga Pernah Di Sekolahin Ya Lu Tolol</b></blockquote>")
    except Exception as error:
        await message.reply(error)



@PY.UBOT("unban", FILTERS.ME_GROUP)
@PY.TOP_CMD
async def admin_unban(client, message):
    gagal = await EMO.GAGAL(client)
    user_id = await extract_user(message)
    if not user_id:
        return await message.reply_text(f"{gagal} Saya Tidak Menemukan Pengguna.")
    try:
        sukses = await EMO.SUKSES(client)
        mention = (await client.get_users(user_id)).mention
    except Exception as error:
        await message.reply(error)
    try:
        await message.chat.unban_member(user_id)
        await message.reply(f"<blockquote><b>{sukses} {mention} Ciee Udah Bisa Gabung Lagi Makannya Jangan Kaya Kontol Biar Ga Di Ban</b></blockquote>")
    except Exception as error:
        await message.reply(error)



@PY.UBOT("staff")
@PY.TOP_CMD
async def staff_cmd(client, message):
    chat_title = message.chat.title
    creator = []
    co_founder = []
    admin = []
    async for x in message.chat.get_members():
        mention = f"<a href=tg://user?id={x.user.id}>{x.user.first_name} {x.user.last_name or ''}</a>"
        if x.status.value == "administrator" and x.privileges and x.privileges.can_promote_members:
            if x.custom_title:
                co_founder.append(f" ┣ {mention} - {x.custom_title}")
            else:
                co_founder.append(f" ┣ {mention}")
        elif x.status.value == "administrator":
            if x.custom_title:
                admin.append(f" ┣ {mention} - {x.custom_title}")
            else:
                admin.append(f" ┣ {mention}")
        elif x.status.value == "owner":
            if x.custom_title:
                creator.append(f" ┗ {mention} - {x.custom_title}")
            else:
                creator.append(f" ┗ {mention}")
    if not co_founder and not admin:
        result = f"""
<b>Staff Group
{chat_title}

👑 Owner:
{creator[0]}</b>"""
    elif not co_founder:
        adm = admin[-1].replace("┣", "┗")
        admin.pop(-1)
        admin.append(adm)
        result = f"""
<b>Staff Group
{chat_title}

:
{creator[0]}

👮 Admin:</b>
""" + "\n".join(
            admin
        )
    elif not admin:
        cof = co_founder[-1].replace(" ┣", " ┗")
        co_founder.pop(-1)
        co_founder.append(cof)
        result = f"""
<b>Staff Group
{chat_title}

👑 Owner:
{creator[0]}

👮 Co Founder:</b>
""" + "\n".join(
            co_founder
        )
    else:
        adm = admin[-1].replace(" ┣", " ┗")
        admin.pop(-1)
        admin.append(adm)
        cof = co_founder[-1].replace(" ┣", " ┗")
        co_founder.pop(-1)
        co_founder.append(cof)
        result = (
            (
                f"""
<b>Staff Group
{chat_title}

👑 Owner:
{creator[0]}

👮 Co Founder:</b>
"""
                + "\n".join(co_founder)
                + """

<b>👮 Admin:</b>
"""
            )
            + "\n".join(admin)
        )

    await message.reply(result)
