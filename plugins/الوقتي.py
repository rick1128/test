# كتابة الشسد : @ZQ_LO
# Repthon - UserBot
# اخمط خوية
# This file is a part of < https://github.com/rogerpq/Repthon/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/rogerpq/Repthon/blob/main/LICENSE/>.

# Ported Plugin

"""
✘ Commands Available -
• `{I}اسم وقتي`
   `لبدء الاسم الوقتي`.
• `{i}انهاء اسم وقتي`
   `لانهاء الاسم.`
• `{i}بايو وقتي`
   `لبدء البايو الوقتي.`
• `{i}انهاء بايو وقتي`
   `لانهاء البايو.`
"""

import random

from telethon.tl.functions.account import UpdateProfileRequest

from . import *

from plugins import ultroid_cmd


@ultroid_cmd(pattern="(اسم وقتي|انهاء اسم وقتي)وقتي$")
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
        name = f"{HM}"
        await event.client(UpdateProfileRequest(last_name=name))
        await asyncio.sleep(1111)


@ultroid_cmd(pattern="(بايو وقتي|انهاء بايو وقتي)$")
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
        name = f"{HM} | {BIOS}"
        await event.client(
            UpdateProfileRequest(
                about=name,
            )
        )
        await asyncio.sleep(1111)


ultroid_bot.loop.create_task(autoname_loop())
ultroid_bot.loop.create_task(autobio_loop())
