from plugins import ultroid_cmd
from telethon import functions, types,events

BAQ = """[ . 𝐑𝐄𝐏𝐓𝐇𝐎𝐍𓌶 - 𝐂𝐌𝐃- .](t.me/Repthon)\n 𓅔 ━━━━━ ━━—×—━━ ━━━━━ 𓅔\n\n - آهـلاً وسـهلاً بك فـي قائـمة أوامـر السـورس [Click here|اضغـط هنـا](https://graph.org/قائمة-اوامر-ريبثون-01-10)\n\n"""


@ultroid_cmd(pattern="الاوامر")
async def hi(event):
    await event.reply(f"{BAQ}")
