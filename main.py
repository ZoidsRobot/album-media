from pyrogram import Client, filters, idle
from pyrogram.types import InputMediaPhoto, Message

API_ID = 9774346
API_HASH = "a92aed7d74654a563af4b07efbcd88e9"
BOT_TOKEN = "6276329771:AAH2a8qTcEU4GaFxpQ062uoG09ndFE7WuSA"

app = Client(name="app", api_id=API_ID, api_hash=API_HASH, bot_token=BOT_TOKEN)

@app.on_message(filters.command("start"))
async def start(c: Client, m: Message):
    await c.send_message(chat_id=m.chat.id, text="Hello! send photo album to me")

@app.on_message(filters.private)
async def handle_album(c: Client, m: Message):
    photos = m.photo.file_id
    await c.send_media_group(chat_id=m.chat.id, media=[InputMediaPhoto(photos) for photo in photos])


app.run()
idle()
