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
from datetime import date, datetime 
import pytz


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
START_MSG = "<b>Hᴇʏ {} Iᴀᴍ Pʀɪᴠᴀᴛᴇ Bᴏᴛ Mᴀꜱᴛᴇʀ Oғ Tᴏ Uꜱᴇ Aᴜᴛᴏ Dᴇʟᴇᴛᴇ Aᴜᴛᴏ Aᴄᴄᴇᴘᴛ Aɴᴅ Mᴏʀᴇ...</b>\n<b>Iᴀᴍ Oғғɪᴄɪᴀʟʏ Wᴏʀᴋɪɴɢ Fᴏʀ Fɪʟɪᴍ Hᴏᴍᴇ Gʀᴏᴜᴘ</b>\n<b>Dᴏɴ'ᴛ Wᴀꜱᴛᴇ Yᴏᴜʀ Tɪᴍᴇ Tᴏ Aᴅᴅɪɴɢ Yᴏᴜʀ Gʀᴏᴜᴘ.. Iᴀᴍ Wᴏʀᴋꜱ Oɴʟʏ Mʏ Gʀᴏᴜᴘ</b>"


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
    add_user(message.from_user.id)
    buttons = [[
        InlineKeyboardButton('Oᴡɴᴇʀ', user_id='1957296068'),
        InlineKeyboardButton('Gʀᴏᴜᴘ', url='https://t.me/MaSTeR_filims')
    ]]
    reply_markup = InlineKeyboardMarkup(buttons)
    await message.reply(
        text=START_MSG.format(message.from_user.mention),
        reply_markup=reply_markup,
        parse_mode=enums.ParseMode.HTML,
    )
    
        
        
@User.on_message(filters.chat(GROUPS))
async def delete(user, message):
    try:
       if message.from_user.id in ADMINS:
          return
       else:
          await User.send_reaction(message.chat.id, message.id, "🔥")
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
            
@Bot.on_message(filters.command("acceptedlist") & filters.user(ADMINS))
async def dbtool(_, m : Message):
    xx = all_users()
    x = all_groups()
    tot = int(xx + x)
    await m.reply_text(text=f"""
🍀 Chats Stats 🍀
🙋‍♂️ Users : `{xx}`
👥 Groups : `{x}`
🚧 Total users & groups : `{tot}` """)
    


@Bot.on_message(filters.command('wt') & filters.user(ADMINS))
async def clean(bot, message):
    data = message.text
    command, nomber = data.split(" ")
    await message.reply_text(f"https://api.whatsapp.com/send?phone={nomber}")

    
        

@Bot.on_message(filters.command("send") & filters.user(ADMINS))
async def deletemultiplefiles(bot, message):
    btn = [[
            InlineKeyboardButton("Tɪᴍᴇ ⏰", callback_data="time"),
            InlineKeyboardButton("Dᴀᴛᴇ 📅", callback_data="date")
          ]]
    await message.reply_text(
        text="<b>Select the type of files you want to delete !\n\nThis will delete 100 files from the database for the selected type.</b>",
        reply_markup=InlineKeyboardMarkup(btn)
    )

    
    
@Bot.on_message(filters.command("bcast") & filters.user(ADMINS))
async def bcast(_, m : Message):
    allusers = users
    lel = await m.reply_text("`⚡️ Processing...`")
    success = 0
    failed = 0
    deactivated = 0
    blocked = 0
    for usrs in allusers.find():
        try:
            userid = usrs["user_id"]
            #print(int(userid))
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
            success +=1
        except FloodWait as ex:
            await asyncio.sleep(ex.value)
            if m.command[0] == "bcast":
                await m.reply_to_message.copy(int(userid))
        except errors.InputUserDeactivated:
            deactivated +=1
            remove_user(userid)
        except errors.UserIsBlocked:
            blocked +=1
        except Exception as e:
            print(e)
            failed +=1

    await lel.edit(f"✅Successfull to `{success}` users.\n❌ Faild to `{failed}` users.\n👾 Found `{blocked}` Blocked users \n👻 Found `{deactivated}` Deactivated users.")

    
  

@Bot.on_message(filters.command('time') & filters.private)
async def start(bot, message):
    try:
       data = message.text
       command, timezone = data.split(" ")
       tz = {timezone}
       today = date.today()
       now = datetime.now(tz)
       time = now.strftime("%H:%M:%S %p")
       await message.reply_text(
           text=(f"today:{today}\ntime: {time}")
       )
    except Exception as e:
       print(e)
    await message.reply_text(f"{e}")
    
    
@Bot.on_message(filters.command('time') & filters.private)
async def start(bot, message):
    msg = await message.reply_text(
        text ='Proccesing'
    )
    await Bot.restart()
    await msg.edit("completed")
  


@Bot.on_message(filters.command('crgrp') & filters.private)
async def start(bot, message):
    await User.create_group("hi", users=ADMINS)
    await User.create_channel("Channel Title", "Channel Description")


    
    
Bot.start()
print("Bot Started!")
User.start()
print("User Started!")

idle()

User.stop()
print("User Stopped!")
Bot.stop()
print("Bot Stopped!")
    
    
