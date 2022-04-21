import asyncio
from time import time
from datetime import datetime
from helpers.filters import command
from pyrogram import Client, filters
from pyrogram.types import Message, InlineKeyboardMarkup, InlineKeyboardButton
from config import (
    BOT_USERNAME,
    OWNER_USERNAME,   
)


@Client.on_message(command(["start"]) & filters.group & ~filters.edited)
async def help(client: Client, message: Message):
    await message.reply_text("**Thanks for adding me im your Group ❤️ Now promote me as a admin with needed powers otherwise I am not able to work properly !!**",
        reply_markup=InlineKeyboardMarkup(
            [
                [
                    InlineKeyboardButton(
                        "⚙️ Source Code", url=f"https://github.com/TheStrayCoder/Music-Streamer")
                ],[
                    InlineKeyboardButton("📨 Support", url=f"https://t.me/StrayCoderSupport"),
                    InlineKeyboardButton("📨 Updates", url=f"https://t.me/StrayCoder")
                  ],
            ]
        ),
    )
