from pyrogram import *
from pyrogram.types import *


# Bot Details

api_id = 20058505
api_hash = "c6416428be72db3174999c1740524b88"
bot_token = "7173891727:AAELOunMmieDp1jJPu-H1m5zlNYZX9SNpBg"

# Initiate the client

app = Client("code", api_id = api_id, api_hash = api_hash, bot_token = bot_token)

# Create a handler for start messge

@app.on_message(filters.command('start')&filters.private)
async def start (client,message):
	await app.send_message(message.chat.id,"__**Hello,\nI am Id generator bot\nJust send me any photo or video and you can see my power ! ! !**__")
	
# Send photo id

@app.on_message(filters.photo & filters.private)
async def photo (bot, message):
	await message.reply_text(message.photo.file_id)
	
# Send video id

@app.on_message(filters.video & filters.private)
async def photo (bot, message):
	await message.reply_text(message.video.file_id)	
	
app.run()