# ""DEAR PRO PEOPLE,  DON'T REMOVE & CHANGE THIS LINE
# TG :- @Mr_Nihal9
#     MY ALL BOTS :- FeelingsXD
#     GITHUB :- MrNihalXd ""

from platform import python_version as y

from pyrogram import __version__ as z
from pyrogram import filters
from pyrogram.types import InlineKeyboardButton, InlineKeyboardMarkup
from telegram import __version__ as o
from telethon import __version__ as s

from Redox import Nihal as pbot

NIHALX = "https://telegra.ph/file/3fd4046e41764142db1a4.jpg"


@pbot.on_message(filters.command("repo"))
async def repo(_, message):
    await message.reply_photo(
        photo=NIHALX,
        caption=f"""✨ **ʜᴇʏ {message.from_user.mention},**

**ᴏᴡɴᴇʀ  : [𝐌ʀ 𝐍ɪʜᴀʟ](https://t.me/Mr_Nihal9)**
**ᴘʏᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{y()}`
**ʟɪʙʀᴀʀʏ ᴠᴇʀꜱɪᴏɴ :** `{o}`
**ᴛᴇʟᴇᴛʜᴏɴ ᴠᴇʀꜱɪᴏɴ :** `{s}`
**ᴘʏʀᴏɢʀᴀᴍ ᴠᴇʀꜱɪᴏɴ :** `{z}`
** ᴇɴᴊᴏʏ**
""",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "•ᴍᴜꜱɪᴄ•", url="https://t.me/Mr_Nihal9"
                    ),
                    InlineKeyboardButton(
                        "•ʀᴏʙᴏᴠ1•", url="https://t.me/Mr_Nihal9"
                    ),
                ]
            ]
        ),
    )
