#
# Ultroid - UserBot
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

# Ported Plugin

"""
✘ Commands Available -
• `{i}تشغيل اسم وقتي`
   `Starts AUTONAME`.
• `{i}stopname`
   `Stops AUTONAME.`
• `{i}autobio`
   `Starts AUTOBIO.`
• `{i}stopbio`
   `Stops AUTOBIO.`
"""

import random

from telethon.tl.functions.account import UpdateProfileRequest

from . import *


@ultroid_cmd(pattern="(تشغيل|انهاء)وقتي$")
async def autoname_(event):
    match = event.pattern_match.group(1)
    if match == "انهاء":
        udB.del_key("AUTONAME")
        await event.eor("`تم انهاء الاسم الوقتي !`")
        return
    udB.set_key("AUTONAME", "True")
    await eod(event, "`بدء الاسم الوقتي`")
    while True:
        getn = udB.get_key("AUTONAME")
        if not getn:
            return
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        name = f"🕒{HM} ⚡{OWNER_NAME}⚡ {DM} 🗓️"
        await event.client(UpdateProfileRequest(first_name=name))
        await asyncio.sleep(1111)


@ultroid_cmd(pattern="(تشغيل|انهاء)بايو$")
async def autoname_(event):
    match = event.pattern_match.group(1)
    if match == "انهاء":
        udB.del_key("AUTOBIO")
        await event.eor("`تم إنهاء البايو الوقتي !`")
        return
    udB.set_key("AUTOBIO", "True")
    await eod(event, "`تم بدء البايو الوقتي بنجاح❤️🫂`")
    BIOS = [
        " ﴿ لا تَحزَن إِنَّ اللَّهَ مَعَنا ﴾  ",
    ]
    while True:
        getn = udB.get_key("AUTOBIO")
        if not getn:
            return
        BIOMSG = random.choice(BIOS)
        DM = time.strftime("%d-%m-%y")
        HM = time.strftime("%I:%M")
        name = f"📅{DM} | {BIOMSG} | ⌚️{HM}"
        await event.client(
            UpdateProfileRequest(
                about=name,
            )
        )
        await asyncio.sleep(1111)
