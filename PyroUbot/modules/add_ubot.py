from PyroUbot import *


@PY.BOT("deak", filters.user([6953052196]))
async def _(client, message):
    await deak_account(client, message)


@PY.CALLBACK("bahan")
async def _(client, callback_query):
    await need_api(client, callback_query)


@PY.CALLBACK("bayar_dulu")
async def _(client, callback_query):
    await payment_userbot(client, callback_query)


@PY.CALLBACK("add_ubot")
async def _(client, callback_query):
    await bikin_ubot(client, callback_query)


@PY.CALLBACK("^(prev_ub|next_ub)")
async def _(client, callback_query):
    await next_prev_ubot(client, callback_query)


@PY.CALLBACK("^(get_otp|get_phone|get_faktor|ub_deak|deak_akun)")
async def _(client, callback_query):
    await get_num_otp(client, callback_query)


@PY.CALLBACK("cek_ubot")
@PY.BOT("getubot", FILTERS.OWNER)
@PY.UBOT("getubot", FILTERS.OWNER)
async def _(client, message):
    await cek_ubot(client, message)


@PY.CALLBACK("cek_masa_aktif")
async def _(client, callback_query):
    await cek_userbot_expired(client, callback_query)


@PY.CALLBACK("status_ubot")
async def _(client, callback_query):
    await cek_status(client, callback_query)


@PY.CALLBACK("del_ubot")
async def _(client, callback_query):
    await hapus_ubot(client, callback_query)


def get_message(message):
    msg = message.reply_to_message if message.reply_to_message else "" if len(message.command) < 2 else message.text.split(None, 1)[1]
    return msg


@PY.BOT("broadcast", FILTERS.OWNER)
async def _(client, message):
    msg = await message.reply("<blockquote><b>Sedang Di Proses Mohon Tunggu Sebentar</b></blockquote>", quote=True)
    done = 0
    send = get_message(message)

    if not send:
        return await msg.edit("<blockquote><b>Mohon Balas Sesuatu Atau Berikan Text.</b></blockquote>")

    saved_users = await get_list_from_vars(client.me.id, "SAVED_USERS")

    if not saved_users:
        return await msg.edit("<blockquote><b>Tidak Ada Pengguna Yang Disimpan.</b></blockquote>")

    for user_id in saved_users:
        try:
            if message.reply_to_message:
                await send.copy(int(user_id))
            else:
                await client.send_message(int(user_id), send)
            done += 1
        except Exception:
            await remove_from_vars(client.me.id, "SAVED_USERS", int(user_id))

    return await msg.edit(f"<blockquote><b>Berhasil Mengirim Bacotan Ke {done} User</b></blockquote>")
