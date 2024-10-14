from PyroUbot import *

__MODULE__ = "Zombies"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Zombies</b></blockquote>

<blockquote><b>๏ Perintah: {0}zombies
◉ Penjelasan: Untuk Menghapus Semua Akun Terhapus Di Grup Anda.</b></blockquote>
"""


@PY.UBOT("zombies")
@PY.TOP_CMD
async def zombies_cmd(client, message):
    chat_id = message.chat.id
    deleted_users = []
    banned_users = 0
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.SUKSES(client)
    Tm = await message.reply(f"{proses} <code>Sedang Memeriksa</code>")
    async for i in client.get_chat_members(chat_id):
        if i.user.is_deleted:
            deleted_users.append(i.user.id)
    if len(deleted_users) > 0:
        for deleted_user in deleted_users:
            try:
                banned_users += 1
                await message.chat.ban_member(deleted_user)
            except Exception:
                pass
        await Tm.edit(f"{sukses} <b>Berhasil Mengeluarkan {banned_users} Akun Hantu</b>")
    else:
        await Tm.edit(f"{gagal} <b>Tidak Ada Akun Hantu Di Group Ini</b>")
