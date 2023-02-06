from os import environ
from pyrogram import idle
from pyrogram.types import Message, InlineKeyboardButton, InlineKeyboardMarkup, CallbackQuery
from pyrogram import Client, filters, errors, enums
from asyncio import sleep
from approvedb import add_user, add_group, all_users, all_groups, users, remove_user
from pyrogram.errors import UserNotParticipant
from pyrogram.errors.exceptions.flood_420 import FloodWait
import random, asyncio
from pyrogram.types import Message, User, ChatJoinRequest
from info import LOG_CHANNEL, ACC_SND_LOG



API_ID = int(environ.get('API_ID', "18302370"))
API_HASH = environ.get('API_HASH', "03c2cced4dea9b1e96dce87558dd2381")
BOT_TOKEN = environ.get('BOT_TOKEN', "6165728582:AAG3XXxjJelE3unp3nbv7bu7Dy-53xVokoY")
SESSION = environ.get('SESSION', "BQC2Tbb3XtDA6WmRTnDlAFkd69IlG0ZZPMZ0bHPr5jpiCjIFnNWj1c2iBgH_yqnRRzJJhVZGSC2N4wLuuDP3oQwgv7yG0lcQtWpjMs8ySO6Azrlg-jMDSFBXBsVilciSj8upUW_DJrjYdEb2K735RYh6T3cTZpMDeQp_Cst4qWcAGNrIQ1b5_mdaz1zm-VGgXkbakCLI8nmHEJppnjWb1usZI8O7QZgWFqrT9mSZJz6zjn7wUDQBsnbjBcKxYZ0xeKDYCp3Wh3N7OqtGMoB69DpWcp2yEZ8wrp2rSe4qCkMnidHN8JKJOplC6TDObxwDRfoy_aTZYZcvdGmQ2LTLBE0IZ6-kngA")
TIME = environ.get('TIME', 600)
GROUPS = []
for grp in environ.get('GROUPS', "-1001784914514").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get('ADMINS', "1957296068").split():
    ADMINS.append(int(usr))
ACC_ALL_CHAT = "-1001866499414"
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
gif = [
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4',
    'https://telegra.ph/file/6d6ad78238403648013c4.mp4',
    'https://telegra.ph/file/7e38c0e9a6b6051199f92.mp4'
]

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

@Bot.on_chat_join_request(filters.group | filters.channel & ~filters.private)
async def approve(client: Bot, message: Message):
    chat=message.chat # Chat
    add_group(chat.id)
    user=message.from_user # User
    print(f"{user.first_name} 𝙹𝙾𝙸𝙽𝙴𝙳 ⚡") # Logs
    await client.approve_chat_join_request(chat_id=chat.id, user_id=user.id)
    img = random.choice(gif)
    add_user(user.id)
    #nothingenter
    await client.send_video(user.id,img, "**Hello {}!\nYour Request To Join {} was approved👍\n\n⚠️click /start to see my power Powered By @sinimapremi **".format(message.from_user.mention, message.chat.title))
    if ACC_SND_LOG == "on":
        await client.send_message(LOG_CHANNEL, "**#New_Approval\n\n Name: {} \n\n Chat: {} \n\n By**".format(message.from_user.mention, message.chat.title))
            
@Bot.on_message(filters.command("users") & filters.user(ADMINS))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)
    
    
User.start()
print("User Started!")
Bot.start()
print("Bot Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
