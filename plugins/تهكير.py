# Repthon - UserBot
# Copyright (C) 2020 RepthonTeam
#
# This file is a part of < https://github.com/rogerpq/Repthon/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/rogerpq/Repthon/blob/main/LICENSE/>.

"""
✘ Commands Available
• `{i}تهكير`
    Do a Prank With Replied user.
"""

import asyncio
import random

from . import *

from plugins import ultroid_cm


@ultroid_cmd(pattern="تهكير")
async def _(event):

if event.reply_to_msg_id:
        reply_message = await event.get_reply_message()
        idd = reply_message.sender_id
        if idd == 5502537272:
            await edit_or_reply(
                event, "**᯽︙ عـذرا لا استـطيع اخـتراق مـطوري اعـتذر او سيقـوم بتهـكيرك**"
            )

    animation_interval = 0.7
    animation_ttl = range(0, 11)
    xx = await event.eor("جار بدء تهكير المستخذم😈")
    animation_chars = [
        "`جار الرفع إلى سيرفر التهكير`",
        "`تم الرفع`",
        "`Installing... 0%\n▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Installing... 4%\n█▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Installing... 8%\n██▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`lnstallig... 20%\n█████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Installing... 36%\n█████████▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Installing... 52%\n█████████████▒▒▒▒▒▒▒▒▒▒▒▒ `",
        "`Installing... 84%\n█████████████████████▒▒▒▒ `",
        "`Installing... 100%\n████████تم التهكير██████████ `",
        "`تم التهكير بنجاح😂😉`",
    ]
