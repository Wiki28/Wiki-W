import os
import re
from platform import python_version as kontol
from telethon import events, Button
from telegram import __version__ as telever
from telethon import __version__ as tlhver
from pyrogram import __version__ as pyrover
from Wiki_W.events import register
from Wiki_W import telethn as tbot


PHOTO = "https://telegra.ph/file/f916bbd6b2d6a1811975b.jpg"

@register(pattern=("/alive"))
async def awake(event):
  GREY = f"**Hi [{event.sender.first_name}](tg://user?id={event.sender.id}), I'm Wiki W.** \n\n"
  GREY += "⚪ **I'm Working Properly** \n\n"
  GREY += f"⚪ **My Master : [Wiki W](https://t.me/terserah_wiki)** \n\n"
  GREY += f"⚪ **Library Version :** `{telever}` \n\n"
  GREY += f"⚪ **Telethon Version :** `{tlhver}` \n\n"
  GREY += f"⚪ **Pyrogram Version :** `{pyrover}` \n\n"
  GREY += "**Thanks For Adding Me Here ❤️**"
  BUTTON = [[Button.url("ʜᴇʟᴘ​", "https://t.me/WikiTapiBot?start=help"), Button.url("sᴜᴘᴘᴏʀᴛ​", "https://t.me/WikiTapiGroup")]]
  await tbot.send_file(event.chat_id, PHOTO, caption=WIKI,  buttons=BUTTON)
