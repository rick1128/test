# Ultroid - UserBot
# Copyright (C) 2021-2022 TeamUltroid
#
# This file is a part of < https://github.com/TeamUltroid/Ultroid/ >
# PLease read the GNU Affero General Public License in
# <https://www.github.com/TeamUltroid/Ultroid/blob/main/LICENSE/>.

from telethon.errors import (
    BotMethodInvalidError,
    ChatSendInlineForbiddenError,
    ChatSendMediaForbiddenError,
)

from . import LOG_CHANNEL, LOGS, Button, asst, eor, get_string, ultroid_cmd

REPOMSG = """
• **REPTHON USERBOT** •\n
• Repo - [اضغـط هنـا](https://github.com/rogerpq/Ultroid)
• الادوات - [Click Here](https://github.com/TeamUltroid/UltroidAddons)
• المساعدة - @Repthon
"""

RP_BUTTONS = [
    [
        Button.url(get_string("bot_3"), "https://github.com/rogerpq/Ultroid"),
        Button.url("Addons", "https://github.com/TeamUltroid/UltroidAddons"),
    ],
    [Button.url("كروب مساعدة", "t.me/Repthon_support")],
]

ULTSTRING = """🎇 **شكرا لك لتنصيب سورس ريبثون!**

• سورس ريبثون يحتوي على كثير من الأوامر اكتشفها بنفسك عن طريق كتابة .الاوامر."""


@ultroid_cmd(
    pattern="الريبو$",
    manager=True,
)
async def repify(e):
    try:
        q = await e.client.inline_query(asst.me.username, "")
        await q[0].click(e.chat_id)
        return await e.delete()
    except (
        ChatSendInlineForbiddenError,
        ChatSendMediaForbiddenError,
        BotMethodInvalidError,
    ):
        pass
    except Exception as er:
        LOGS.info(f"Error while repo command : {str(er)}")
    await e.eor(REPOMSG)


@ultroid_cmd(pattern="ريبثون$")
async def useUltroid(rs):
    button = Button.inline("Start >>", "initft_2")
    msg = await asst.send_message(
        LOG_CHANNEL,
        ULTSTRING,
        file="https://graph.org/file/b3e0cb631d36672092852.jpg",
        buttons=button,
    )
    if not (rs.chat_id == LOG_CHANNEL and rs.client._bot):
        await eor(rs, f"**[اضغـط هنـا]({msg.message_link})**")
