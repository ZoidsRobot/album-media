from pyrogram import Client, filters, idle
from pyrogram.types import InputMediaPhoto, Message

API_ID = 0
API_HASH = "asdfh"
BOT_TOKEN = "12345:asdfg"

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
