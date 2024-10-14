
from .. import *

__MODULE__ = "Sudo"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Sudo

<blockquote><b>๏ Perintah: {0}addsudo
◉ Penjelasan: Untuk Menambahkan User Ke Dalam Daftar Sudo</b></blockquote>
<blockquote><b>๏ Perintah: {0}delsudo
◉ Penjelasan: Untuk Menghapus User Dari Daftar Sudo</b></blockquote>
<blockquote><b>๏ Perintah:{0}getsudo
◉ Penjelasan: Untuk Melihat Daftar Sudo</b></blockquote>
"""


@PY.UBOT("addsudo")
@PY.TOP_CMD
async def _(client, message):
    msg = await message.reply("<blockquote>🔄 Sabar Ya Jink...</blockquote>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit("<blockquote><b>Harap Balas Ke User Yang Mau Di Tambahkan Ke Daftar Sudo</b></blockquote>")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")

    if user.id in sudo_users:
        return await msg.edit(f"<blockquote><b> [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) Sudah Berada Di Dalam Daftar Sudo</b></blockquote>")

    try:
        await add_to_vars(client.me.id, "SUDO_USERS", user.id)
        return await msg.edit(f"<blockquote><b>✅ [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) Berhasil Di Tambahkan Ke Daftar Sudo</b></blockquote>")
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("delsudo")
@PY.TOP_CMD
async def _(client, message):
    msg = await message.reply("<blockquote><b>🔄 Sabar Ya Jink...</b></blockquote>")
    user_id = await extract_user(message)
    if not user_id:
        return await msg.edit("<blockquote><b>➡️ Harap Masukan User Yang Mau Di Hapus Dari Daftar Sudo</b></blockquote>")

    try:
        user = await client.get_users(user_id)
    except Exception as error:
        return await msg.edit(error)

    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")

    if user.id not in sudo_users:
        return await message.reply(f"<blockquote><b>✨ [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) Tidak Ada Di Dalam Daftar Sudo</b></blockquote>")

    try:
        await remove_from_vars(client.me.id, "SUDO_USERS", user.id)
        return await msg.edit(f"<blockquote><b>❌ [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) Berhasil Di Hapus Dari Daftar Sudo</b></blockquote>")
    except Exception as error:
        return await msg.edit(error)


@PY.UBOT("getsudo")
@PY.TOP_CMD
async def _(client, message):
    msg = await message.reply("<blockquote><b>🔄 Sabar Ya Jink...</b></blockquote>")
    sudo_users = await get_list_from_vars(client.me.id, "SUDO_USERS")

    if not sudo_users:
        return await msg.edit("<s>Daftar Sudo Kosong</s>")

    sudo_list = []
    for user_id in sudo_users:
        try:
            user = await client.get_users(int(user_id))
            sudo_list.append(f" ├ [{user.first_name} {user.last_name or ''}](tg://user?id={user.id}) | <code>{user.id}</code>")
        except:
            continue

    if sudo_list:
        response = "<b>❏ Daftar Sudo:</b>\n" + "\n".join(sudo_list) + f"\n <b>╰ Total Sudo User:</b> <code>{len(sudo_list)}</code>"
        return await msg.edit(response)
    else:
        return await msg.edit("<b>Tidak Dapat Mengambil Daftar Sudo Saat Ini</b>")
