from telethon import __version__, events, Button

from config import X1, X2, X3, X4, X5, X6, X7, X8, X9, X10


START_BUTTON = [
    [
        Button.inline("⛈◄⏤ 𝐂ᴏᴍᴍᴀɴᴅꜱ ◄⏤⛈", data="help_back")
    ],
    [
        Button.url("⛈◄⏤ 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ◄⏤⛈", "https://t.me/Taha_khan_op"),
        Button.url("⛈◄⏤ 𝗦𝘂𝗽𝗽𝗼𝗿𝘁◄⏤⛈", "https://t.me/indianlok")
    ],
    [
        Button.url("⛈◄⏤ 𝗗𝗲𝘃𝗲𝗹𝗼𝗽𝗲𝗿 ◄⏤⛈", "https://t.me/Taha_khan_op")

        
    ]
]


@X1.on(events.NewMessage(pattern="/start"))
@X2.on(events.NewMessage(pattern="/start"))
@X3.on(events.NewMessage(pattern="/start"))
@X4.on(events.NewMessage(pattern="/start"))
@X5.on(events.NewMessage(pattern="/start"))
@X6.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X7.on(events.NewMessage(pattern="/start"))
@X8.on(events.NewMessage(pattern="/start"))
@X9.on(events.NewMessage(pattern="/start"))
@X10.on(events.NewMessage(pattern="/start"))
async def start(event):              
    if event.is_private:
        AltBot = await event.client.get_me()
        bot_name = AltBot.first_name
        bot_id = AltBot.id
        TEXT = f"**ʜᴇʏ​ [{event.sender.first_name}](tg://user?id={event.sender.id}),\n\nɪ ᴀᴍ [{bot_name}](tg://user?id={bot_id})​**\n━━━━━━━━━━━━━━━━━━━\n\n"
        TEXT += f"» **𝐌𝐘 𝐃𝐄𝐕𝐄𝐋𝐎𝐏𝐄𝐑 : [⛈𝗖𝗢𝗗𝗘𝗥⛈](https://t.me/Taha_khan_op) **\n\n"
        TEXT += f"» **𝐁𝐎𝐓𝐒 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 :** `M3.3`\n"
        TEXT += f"» **𝐏𝐘𝐓𝐇𝐎𝐍 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 :** `3.11.3`\n"
        TEXT += f"» **𝗧𝗔𝗛𝗔 𝐕𝐄𝐑𝐒𝐈𝐎𝐍 :** `{__version__}`\n━━━━━━━━━━━━━━━━━"
        await event.client.send_file(
                    event.chat_id,
                    "https://graph.org/file/5d534d7a34d126e65168f.jpg",
                    caption=TEXT, 
                    buttons=START_BUTTON
                )
