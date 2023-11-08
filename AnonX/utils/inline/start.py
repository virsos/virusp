from typing import Union

from pyrogram.types import InlineKeyboardMarkup, InlineKeyboardButton

import config
from config import SUPPORT_CHANNEL



def start_pannel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="‹ اضفني لمجموعتك ›",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="‹ الاوامر ›",
                callback_data="settings_back_helper",
            ),
            InlineKeyboardButton(
                text="المساعدة", callback_data="settings_helper"
            ),
        ],
     ]
    return buttons


def private_panel(_, BOT_USERNAME, OWNER: Union[bool, int] = None):
    buttons = [
        [
            InlineKeyboardButton(
                text="‹ اضفني لمجموعتك ›",
                url=f"https://t.me/{BOT_USERNAME}?startgroup=true",
            )
        ],
        [
            InlineKeyboardButton(
                text="‹ الاوامر ›", callback_data="settings_back_helper"
            )
        ],
        [
            InlineKeyboardButton(
                text="‹ لشراء بوت ›", url=f"https://t.me/IIIlIIv"
            ),
            InlineKeyboardButton(
                text="‹ مطور البوت ›", user_id=OWNER
            )
        ],
        [
            InlineKeyboardButton(
                text="‹ قناة السورس ›", url=f"https://t.me/{SUPPORT_CHANNEL}"
            )
        ],
      
     ]
    return buttons
