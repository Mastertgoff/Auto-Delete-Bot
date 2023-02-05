import asyncio
from os import environ
from pyrogram import Client, filters, idle
from pyrogram import approve_all_chat_join_requests

API_ID = int(environ.get('API_ID', "18302370"))
API_HASH = environ.get('API_HASH', "03c2cced4dea9b1e96dce87558dd2381")
BOT_TOKEN = environ.get('BOT_TOKEN', "6165728582:AAG3XXxjJelE3unp3nbv7bu7Dy-53xVokoY")
SESSION = environ.get('SESSION', "BQC2Tbb3XtDA6WmRTnDlAFkd69IlG0ZZPMZ0bHPr5jpiCjIFnNWj1c2iBgH_yqnRRzJJhVZGSC2N4wLuuDP3oQwgv7yG0lcQtWpjMs8ySO6Azrlg-jMDSFBXBsVilciSj8upUW_DJrjYdEb2K735RYh6T3cTZpMDeQp_Cst4qWcAGNrIQ1b5_mdaz1zm-VGgXkbakCLI8nmHEJppnjWb1usZI8O7QZgWFqrT9mSZJz6zjn7wUDQBsnbjBcKxYZ0xeKDYCp3Wh3N7OqtGMoB69DpWcp2yEZ8wrp2rSe4qCkMnidHN8JKJOplC6TDObxwDRfoy_aTZYZcvdGmQ2LTLBE0IZ6-kngA")
TIME = "900"
GROUPS = []
for grp in environ.get('GROUPS', "-1001784914514").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get('ADMINS', "1957296068").split():
    ADMINS.append(int(usr))
ACC_ALL_CHAT = "-1001869891071"
START_MSG = "<b>Hai {},\nI'm a private bot of MaSTeR to delete group messages after a specific time</b>"


User = Client(name="user-account",
              session_string=SESSION,
              api_id=API_ID,
              api_hash=API_HASH,
              workers=300
              )


Bot = Client(name="auto-delete",
             api_id=API_ID,
             api_hash=API_HASH,
             bot_token=BOT_TOKEN,
             workers=300
             )


@Bot.on_message(filters.command('start') & filters.private)
async def start(bot, message):
    await message.reply(START_MSG.format(message.from_user.mention))

@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await asyncio.sleep(TIME)
          await Bot.delete_messages(message.chat.id, message.id)
    except Exception as e:
       print(e)
    
@Bot.on_message(filters.command("run") & filters.user(ADMINS) & filters.private)
async def accept(bot, message):
    lol = await message.reply_text(
        text ='Proccesing'
    )
    chat=ACC_ALL_CHAT # Chat
    user=message.from_user # User
    await User.approve_all_chat_join_requests(chat_id=ACC_ALL_CHAT)
    await lol.edit(f"Completed")
    print("Completed")
    
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
