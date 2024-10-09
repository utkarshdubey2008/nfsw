# Copyright 2024 Qewertyy, MIT License

from pyrogram import Client, filters, types as t
from bot import StartTime

startText = ```
HELLO 👋 I AM ADULT CONTENT DETECTOR BOT.I CAN DETECT ADULT CONTENT IN YOUR GROUPS AND PREVENT THEM FROM BEING BANNED
```

@Client.on_message(filters.command(["start","help","support","channel"]))
async def start(_: Client, m: t.Message):
    await m.reply_text(
        startText,
        reply_markup=t.InlineKeyboardMarkup(
            [
                [
                    t.InlineKeyboardButton(text="support",url="https:t.me/Thealphabotz")
                ]
            ]
        )
    )
