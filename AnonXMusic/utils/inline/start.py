from pyrogram.types import InlineKeyboardButton

import config
from AnonXMusic import app


def start_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="» Aᴅᴅ ᴍᴇ ʙᴀʙʏ «", url=f"https://t.me/{app.username}?startgroup=true"
            ),
            InlineKeyboardButton(text="•ɢʀᴏᴜᴩ•", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons


def private_panel(_):
    buttons = [
        [
            InlineKeyboardButton(
                text="» Aᴅᴅ ᴍᴇ ʙᴀʙʏ «",
                url=f"https://t.me/{app.username}?startgroup=true",
            )
        ],
        [InlineKeyboardButton(text="•Mᴏɪ ᴏᴡɴᴇʀ•", user_id=config.OWNER_ID)],
        [
            InlineKeyboardButton(text="•ʜᴇʟᴩ•", callback_data="settings_back_helper"),
            InlineKeyboardButton(text="•ɢʀᴏᴜᴩ•", url=config.SUPPORT_CHAT),
        ],
    ]
    return buttons
