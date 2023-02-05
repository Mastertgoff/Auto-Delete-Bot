import asyncio
from os import environ
from pyrogram import Client, filters, idle

API_ID = int(environ.get('API_ID', "18302370"))
API_HASH = environ.get('API_HASH', "03c2cced4dea9b1e96dce87558dd2381")
BOT_TOKEN = environ.get('BOT_TOKEN', "5838549524:AAHzJBsy6q3KXniWAqyyd_qrcQu130_aXPU")
SESSION = environ.get('SESSION', "BQBylaS31dBMNWABt_-plJ3Rb54AtTpq5JWCUZ0MvmPeogebg-hv0cSmGHbD0l46Oy2aIpUyeitDew93nWAHZ3jGgE_oH4rzVUSytywBVi19KpJS7tglb49FNmdmzj5xBymrUEvAQUrIMAN5-vIvvpbKj1srWofiuNeaBxGD_8XQlagtDruxj9YVHuL3YwFESkHPrCzEG0VxJys4pOy3YCq9uniYPLIVhAmNQPtQl2fR3lx6ZEU4vGiZdJZ6ZzXqKcyfdhuJaEpXBQmHaOF8LeDI7her8eEqqTduYZvQKK1Ccsb7q7LnLWTjWZBIJuHdwnTooiZjRTS9n5GYrOBgW5SFAAAAAWFsnJgA")
TIME = int(environ.get("TIME"))
GROUPS = []
for grp in environ.get('GROUPS', "-1001784914514").split():
    GROUPS.append(int(grp))
ADMINS = []
for usr in environ.get('ADMINS', "1957296068").split():
    ADMINS.append(int(usr))

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
    await User.approve_all_chat_join_requests(chat_id=chat.id, user_id=user.id)
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
