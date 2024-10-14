from telegraph import Telegraph, exceptions, upload_file

from PyroUbot import *

__MODULE__ = "Telegraph"
__HELP__ = """
<blockquote><b>✘ Bantuan Untuk Telegraph</b></blockquote>

<blockquote><b>๏ Perintah: {0}tg [Reply Media/Text]
◉ Penjelasan: Untuk Mengupload Media/Text Ke Telegraph</b></blockquote>
"""



@PY.UBOT("tg")
@PY.TOP_CMD
async def tg_cmd(client, message):
    proses = await get_vars(client.me.id, "EMOJI_PROSES") or "5960640164114993927"
    XD = await message.reply(f"<b><emoji id={proses}>⏳</emoji><code>Processing....</code>")
    if not message.reply_to_message:
        return await XD.edit("<b>Mohon Balas Ke Pesan, Untuk Mendapatkan Link Dari Telegraph.</b>")
    telegraph = Telegraph()
    if message.reply_to_message.media:
        m_d = await dl_pic(client, message.reply_to_message)
        try:
            media_url = upload_file(m_d)
        except exceptions.TelegraphException as exc:
            return await XD.edit(f"<code>{exc}</code>")
        sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
        U_done = f"<blockquote><b><emoji id={sukses}>✅</emoji> Berhasil Di Upload Ke <a href='https://telegra.ph/{media_url[0]}'>Telegraph</a></b></blockquote>"
        await XD.edit(U_done)
    elif message.reply_to_message.text:
        page_title = f"{client.me.first_name} {client.me.last_name or ''}"
        page_text = message.reply_to_message.text
        page_text = page_text.replace("\n", "<br>")
        try:
            response = telegraph.create_page(page_title, html_content=page_text)
        except exceptions.TelegraphException as exc:
            return await XD.edit(f"<code>{exc}</code>")
        sukses = await get_vars(client.me.id, "EMOJI_SUKSES") or "5787188704434982946"
        wow_graph = f"<blockquote><b><emoji id={sukses}>✅</emoji> Berhasil Di Upload Ke <a href='https://telegra.ph/{response['path']}'>Telegraph</a></b></blockquote>"
        await XD.edit(wow_graph)
