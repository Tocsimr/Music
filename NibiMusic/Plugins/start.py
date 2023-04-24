import asyncio
import random
from NibiMusic.config import BOT_USERNAME, OWNER_USERNAME, UPDATE_CHANNEL, SUPPORT_GROUP
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton


NIBI_IMG = (
"https://te.legra.ph/file/1b82afbf90d074849136e.jpg",
"https://te.legra.ph/file/0f64be1cf523f76aa0e2e.jpg",
"https://te.legra.ph/file/1bedd3d90170cc6da5282.jpg",
"https://te.legra.ph/file/c18b4ff72e93a1def1eef.jpg",
"https://te.legra.ph/file/43b1aff6ba286cd61b4cc.jpg",
"https://te.legra.ph/file/45f301147ffede1856f0d.jpg",
"https://te.legra.ph/file/40f551a935da47f59ff64.jpg",

)





START_TEXT = """
ʜɪ ɢᴜʏꜱ, ɪ ᴀᴍ ᴠᴇʀʏ ʜɪɢʜʟʏ ᴀ.ɪ ᴀᴅᴠᴀɴᴄᴇᴅ ɴᴇxᴛ ɢᴇɴᴇʀᴀᴛɪᴏɴ ᴠᴄ ʙᴏᴛ.
ɪ' ᴍ ᴠᴇʀʏ ғᴀꜱᴛ ᴀɴᴅ ᴍᴏʀᴇ ᴇꜰꜰɪᴄɪᴇɴᴛ ɪ ᴘʀᴏᴠɪᴅᴇ ᴀᴡᴇꜱᴏᴍᴇ ꜱᴏᴜɴᴅ ǫᴜᴀʟɪᴛʏ !
"""

    
   
