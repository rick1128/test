# كتابة الشسد : @ZQ_LO
# اخمطططططططططططططططط
# انسخخخخخخخخخخخخخخخخخخخخ


"""
✘ Commands Available -
• `{i}<شخصية>   <اسم الشخصية.>`
   شخصية. ليضهر لك معلومات عن شخصية انمي
"""

import jikanpy

from . import *


@ultroid_cmd(pattern="شخصية ?(.*)")
async def anime_char_search(event):
    xx = await event.eor(get_string("com_1"))
    char_name = event.pattern_match.group(1)
    if not char_name:
        await eod(xx, "`خطأ قم بكتابة اسم الشخصية😕`", time=5)
    jikan = jikanpy.jikan.Jikan()
    try:
        s = jikan.search("character", char_name)
    except jikanpy.exceptions.APIException:
        return await eod(xx, "`Couldn't find character!`", time=5)
    a = s["results"][0]["mal_id"]
    char_json = jikan.character(a)
    pic = char_json["image_url"]
    msg = f"**[{char_json['name']}]({char_json['url']})**"
    if char_json["name_kanji"] != "Japanese":
        msg += f" [{char_json['name_kanji']}]\n"
    else:
        msg += "\n"
    if char_json["Nicknames"]:
        nicknames_string = ", ".join(char_json["nicknames"])
        msg += f"\n**الاسم** : `{nicknames_string}`\n"
    about = char_json["about"].split("\n", 1)[0].strip().replace("\n", "")
    msg += f"\n**المعلومات**: __{about}__"
    await event.reply(msg, file=pic, force_document=False)
    await xx.delete()
