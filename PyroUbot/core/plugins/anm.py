import asyncio
import random

import requests
from pyrogram import *
from pyrogram.errors.exceptions.flood_420 import FloodWait
from pyrogram.types import *

from PyroUbot import *

DEFAULTUSER = "Nay"


NOBLE = [
    "╲╲╲┏━━┓╭━━━╮╱╱╱\n╲╲╲┗┓┏┛┃╭━╮┃╱╱╱\n╲╲╲╲┃┃┏┫┃╭┻┻┓╱╱\n╱╱╱┏╯╰╯┃╰┫┏━╯╱╱\n╱╱┏┻━┳┳┻━┫┗┓╱╱╱\n╱╱╰━┓┃┃╲┏┫┏┛╲╲╲\n╱╱╱╱┃╰╯╲┃┃┗━╮╲╲\n╱╱╱╱╰━━━╯╰━━┛╲╲",
    "┏━╮\n┃▔┃▂▂┏━━┓┏━┳━━━┓\n┃▂┣━━┻━╮┃┃▂┃▂┏━╯\n┃▔┃▔╭╮▔┃┃┃▔┃▔┗━┓\n┃▂┃▂╰╯▂┃┗╯▂┃▂▂▂┃\n┃▔┗━━━╮┃▔▔▔┃▔┏━╯\n┃▂▂▂▂▂┣╯▂▂▂┃▂┗━╮\n┗━━━━━┻━━━━┻━━━┛",
    "┏┓┏━┳━┳━┳━┓\n┃┗┫╋┣┓┃┏┫┻┫\n┗━┻━┛┗━┛┗━┛\n────­­­­­­­­­YOU────",
    "╦──╔╗─╗╔─╔ ─\n║──║║─║║─╠ ─\n╚═─╚╝─╚╝─╚ ─\n╦─╦─╔╗─╦╦   \n╚╦╝─║║─║║ \n─╩──╚╝─╚╝",
    "╔══╗....<3 \n╚╗╔╝..('\\../') \n╔╝╚╗..( •.• ) \n╚══╝..(,,)(,,) \n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "░I░L░O░V░E░Y░O░U░",
    "┈┈╭━╱▔▔▔▔╲━╮┈┈┈\n┈┈╰╱╭▅╮╭▅╮╲╯┈┈┈\n╳┈┈▏╰┈▅▅┈╯▕┈┈┈┈\n┈┈┈╲┈╰━━╯┈╱┈┈╳┈\n┈┈┈╱╱▔╲╱▔╲╲┈┈┈┈\n┈╭━╮▔▏┊┊▕▔╭━╮┈╳\n┈┃┊┣▔╲┊┊╱▔┫┊┃┈┈\n┈╰━━━━╲╱━━━━╯┈╳",
    "╔ღ═╗╔╗\n╚╗╔╝║║ღ═╦╦╦═ღ\n╔╝╚╗ღ╚╣║║║║╠╣\n╚═ღ╝╚═╩═╩ღ╩═╝",
    "╔══╗ \n╚╗╔╝ \n╔╝(¯'v'¯) \n╚══'.¸./\n╔╗╔═╦╦╦═╗ ╔╗╔╗ \n║╚╣║║║║╩╣ ║╚╝║ \n╚═╩═╩═╩═╝ ╚══╝",
    "╔╗ \n║║╔═╦═╦═╦═╗ ╔╦╗ \n║╚╣╬╠╗║╔╣╩╣ ║║║ \n╚═╩═╝╚═╝╚═╝ ╚═╝ \n╔═╗ \n║═╬═╦╦╦═╦═╦═╦═╦═╗ \n║╔╣╬║╔╣╩╬╗║╔╣╩╣╔╝ \n╚╝╚═╩╝╚═╝╚═╝╚═╩╝",
    "╔══╗ \n╚╗╔╝ \n╔╝╚╗ \n╚══╝ \n╔╗ \n║║╔═╦╦╦═╗ \n║╚╣║║║║╚╣ \n╚═╩═╩═╩═╝ \n╔╗╔╗ ♥️ \n║╚╝╠═╦╦╗ \n╚╗╔╣║║║║ \n═╚╝╚═╩═╝",
    "╔══╗╔╗  ♡ \n╚╗╔╝║║╔═╦╦╦╔╗ \n╔╝╚╗║╚╣║║║║╔╣ \n╚══╝╚═╩═╩═╩═╝\n­­­─────­­­­­­­­­YOU─────",
    "╭╮╭╮╮╭╮╮╭╮╮╭╮╮ \n┃┃╰╮╯╰╮╯╰╮╯╰╮╯ \n┃┃╭┳━━┳━╮╭━┳━━╮ \n┃┃┃┃╭╮┣╮┃┃╭┫╭╮┃ \n┃╰╯┃╰╯┃┃╰╯┃┃╰┻┻╮ \n╰━━┻━━╯╰━━╯╰━━━╯",
    "┊┊╭━╮┊┊┊┊┊┊┊┊┊┊┊ \n━━╋━╯┊┊┊┊┊┊┊┊┊┊┊ \n┊┊┃┊╭━┳╮╭┓┊╭╮╭━╮ \n╭━╋━╋━╯┣╯┃┊┃╰╋━╯ \n╰━╯┊╰━━╯┊╰━┛┊╰━━",
]


async def lopeyo(client, message):
    noble = random.randint(1, len(NOBLE) - 2)
    reply_text = NOBLE[noble]
    await message.reply(reply_text)



async def hmmm(client, message):
    mg = await message.reply(
        "┈┈╱▔▔▔▔▔╲┈┈┈HM┈HM\n┈╱┈┈╱▔╲╲╲▏┈┈┈HMMM\n╱┈┈╱━╱▔▔▔▔▔╲━╮┈┈\n▏┈▕┃▕╱▔╲╱▔╲▕╮┃┈┈\n▏┈▕╰━▏▊▕▕▋▕▕━╯┈┈\n╲┈┈╲╱▔╭╮▔▔┳╲╲┈┈┈\n┈╲┈┈▏╭━━━━╯▕▕┈┈┈\n┈┈╲┈╲▂▂▂▂▂▂╱╱┈┈┈\n┈┈┈┈▏┊┈┈┈┈┊┈┈┈╲\n┈┈┈┈▏┊┈┈┈┈┊▕╲┈┈╲\n┈╱▔╲▏┊┈┈┈┈┊▕╱▔╲▕\n┈▏┈┈┈╰┈┈┈┈╯┈┈┈▕▕\n┈╲┈┈┈╲┈┈┈┈╱┈┈┈╱┈╲\n┈┈╲┈┈▕▔▔▔▔▏┈┈╱╲╲╲▏\n┈╱▔┈┈▕┈┈┈┈▏┈┈▔╲▔▔\n┈╲▂▂▂╱┈┈┈┈╲▂▂▂╱┈ ",
    )



async def ror(client, message):
    e = await message.reply("**ROOORRR**")
    await asyncio.sleep(1.5)
    await e.edit("**ROOORRR AAHHH**")
    await asyncio.sleep(1.5)
    await e.edit("**ROOORRR AAHHHH AAHHH**")
    await asyncio.sleep(1.5)
    await e.edit("**ROOORRR AAHHHH AAHHHH AAHHHH**")
    await asyncio.sleep(1.5)
    await e.edit("**ROOORRR AAHHHH AAHHHH AAHHHH AAHHHH**")



async def fucek(client, message):
    await message.reply(
        "░░░░░░░░░░░░░░░▄▄░░░░░░░░░░░\n"
        "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
        "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
        "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
        "░░░░░░░░░░░░░░█░░█░░░░░░░░░░\n"
        "██████▄███▄████░░███▄░░░░░░░\n"
        "▓▓▓▓▓▓█░░░█░░░█░░█░░░███░░░░\n"
        "▓▓▓▓▓▓█░░░█░░░█░░█░░░█░░█░░░\n"
        "▓▓▓▓▓▓█░░░░░░░░░░░░░░█░░█░░░\n"
        "▓▓▓▓▓▓█░░░░░░░░░░░░░░░░█░░░░\n"
        "▓▓▓▓▓▓█░░░░░░░░░░░░░░██░░░░░\n"
        "▓▓▓▓▓▓█████░░░░░░░░░██░░░░░░\n"
    )



async def helikopter(client, message):
    await message.reply(
        "▬▬▬.◙.▬▬▬ \n"
        "═▂▄▄▓▄▄▂ \n"
        "◢◤ █▀▀████▄▄▄▄◢◤ \n"
        "█▄ █ █▄ ███▀▀▀▀▀▀▀╬ \n"
        "◥█████◤ \n"
        "══╩══╩══ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ \n"
        "╬═╬ Hallo Semuanya :) \n"
        "╬═╬☻/ \n"
        "╬═╬/▌ \n"
        "╬═╬/ \\ \n",
    )



async def dornembak(client, message):
    await message.reply(
        "_/﹋\\_\n" "(҂`_´)\n" "<,︻╦╤─ ҉\n" r"_/﹋\_" "\n<b>Mau Jadi Pacarku Gak?!</b>",
    )



async def ngebundir(client, message):
    await message.reply(
        "`Dadah Semuanya...`          \n　　　　　|"
        "\n　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　　　　　| \n"
        "　／￣￣＼| \n"
        "＜ ´･ 　　 |＼ \n"
        "　|　３　 | 丶＼ \n"
        "＜ 、･　　|　　＼ \n"
        "　＼＿＿／∪ _ ∪) \n"
        "　　　　　 Ｕ Ｕ\n",
    )



async def awikwok(client, message):
    await message.reply(
        "────██──────▀▀▀██\n"
        "──▄▀█▄▄▄─────▄▀█▄▄▄\n"
        "▄▀──█▄▄──────█─█▄▄\n"
        "─▄▄▄▀──▀▄───▄▄▄▀──▀▄\n"
        "─▀───────▀▀─▀───────▀▀\n`Awkwokwokwok..`",
    )



async def ysaja(client, message):
    await message.reply(
        "‡‡‡‡‡‡‡‡‡‡‡‡▄▄▄▄\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡‡█‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡‡█‡‡‡‡‡█\n"
        "‡‡‡‡‡‡‡‡‡█‡‡‡‡‡‡█\n"
        "██████▄▄█‡‡‡‡‡‡████████▄\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡‡█\n"
        "▓▓▓▓▓▓█████‡‡‡‡‡‡‡‡‡‡‡‡██\n"
        "█████‡‡‡‡‡‡‡██████████\n",
    )


async def tank(client, message):
    await message.reply(
        "█۞███████]▄▄▄▄▄▄▄▄▄▄▃ \n"
        "▂▄▅█████████▅▄▃▂…\n"
        "[███████████████████]\n"
        "◥⊙▲⊙▲⊙▲⊙▲⊙▲⊙▲⊙◤\n",
    )


async def babi(client, message):
    await message.reply(
        "┈┈┏━╮╭━┓┈╭━━━━╮\n"
        "┈┈┃┏┗┛┓┃╭┫Ngok ┃\n"
        "┈┈╰┓▋▋┏╯╯╰━━━━╯\n"
        "┈╭━┻╮╲┗━━━━╮╭╮┈\n"
        "┈┃▎▎┃╲╲╲╲╲╲┣━╯┈\n"
        "┈╰━┳┻▅╯╲╲╲╲┃┈┈┈\n"
        "┈┈┈╰━┳┓┏┳┓┏╯┈┈┈\n"
        "┈┈┈┈┈┗┻┛┗┻┛┈┈┈┈\n",
    )


async def piciieess(client, message):
    e = await message.edit("**Ayanggg 😖**")
    await asyncio.sleep(2)
    await e.edit("**Aku Ange 😫**")
    await asyncio.sleep(2)
    await e.edit("**Ayuukk Picies Yang 🤤**")


async def lipkoll(client, message):
    e = await message.edit("**Ayanggg 😖**")
    await asyncio.sleep(2)
    await e.edit("**Kangeeen 👉👈**")
    await asyncio.sleep(2)
    await e.edit("**Pingiinn Slipkool Yaaang🥺👉👈**")


async def nakall(client, message):
    e = await message.edit("**Ayanggg ih🥺**")
    await asyncio.sleep(2)
    await e.edit("**Nakal Banget Dah Ayang🥺**")
    await asyncio.sleep(2)
    await e.edit("**Aku Gak Like Ayang😠**")
    await asyncio.sleep(2)
    await e.edit("**Pokoknya Aku Gak Like Ih😠**")


async def peace(client: Client, message: Message):
    await message.reply(
        "┈┈┈┈PEACE MAN┈┈┈┈\n"
        "┈┈┈┈┈┈╭╮╭╮┈┈┈┈┈┈\n"
        "┈┈┈┈┈┈┃┃┃┃┈┈┈┈┈┈\n"
        "┈┈┈┈┈┈┃┃┃┃┈┈┈┈┈┈\n"
        "┈┈┈┈┈┈┃┗┛┣┳╮┈┈┈┈\n"
        "┈┈┈┈┈╭┻━━┓┃┃┈┈┈┈\n"
        "┈┈┈┈┈┃╲┏━╯┻┫┈┈┈┈\n"
        "┈┈┈┈┈╰╮╯┊┊╭╯┈┈┈┈\n",
    )


async def spongebobss(client: Client, message: Message):
    await message.reply(
        "╲┏━┳━━━━━━━━┓╲╲\n"
        "╲┃◯┃╭┻┻╮╭┻┻╮┃╲╲\n"
        "╲┃╮┃┃╭╮┃┃╭╮┃┃╲╲\n"
        "╲┃╯┃┗┻┻┛┗┻┻┻┻╮╲\n"
        "╲┃◯┃╭╮╰╯┏━━━┳╯╲\n"
        "╲┃╭┃╰┏┳┳┳┳┓◯┃╲╲\n"
        "╲┃╰┃◯╰┗┛┗┛╯╭┃╲╲\n",
    )


async def kocokk(client, message):
    e = await message.reply("KOCOKINNNN SAYANGG🥵")
    await asyncio.sleep(0.2)
    await e.edit("8✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8✊===D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D💦")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8✊===D💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8=✊==D💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8✊===D💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8===✊D💦💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("8==✊=D💦💦💦💦💦💦💦💦💦💦")
    await asyncio.sleep(0.2)
    await e.edit("**CROOTTTT**")
    await asyncio.sleep(0.2)
    await e.edit("**CROOTTTT AAAHHH.....**")
    await asyncio.sleep(0.2)
    await e.edit("**AHHH ENAKKKKK SAYANGGGG🥵🥵**")


async def anjg(client, message):
    await message.reply(
        "╥━━━━━━━━╭━━╮━━┳\n"
        "╢╭╮╭━━━━━┫┃▋▋━▅┣\n"
        "╢┃╰┫┈┈┈┈┈┃┃┈┈╰┫┣\n"
        "╢╰━┫┈┈┈┈┈╰╯╰┳━╯┣\n"
        "╢┊┊┃┏┳┳━━┓┏┳┫┊┊┣\n"
        "╨━━┗┛┗┛━━┗┛┗┛━━┻\n",
    )



async def nahlove(client, message):
    typew = await message.reply("`\n(\\_/)`" "`\n(●_●)`" "`\n />💖 **Ini Buat Kamu**")
    await asyncio.sleep(2)
    await typew.edit("`\n(\\_/)`" "`\n(●_●)`" "`\n💖<\\  **Tapi Bo'ong**")
