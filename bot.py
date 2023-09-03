import os
from pyrogram import Client, filters

api_id = int(os.environ.get("API_ID"))
api_hash = os.environ.get("API_HASH")
bot_token = os.environ.get("BOT_TOKEN")

bot = Client("test_bot", api_id=api_id, api_hash=api_hash, bot_token=bot_token)

@bot.on_message(filters.command("start"))
async def start(client, message):
    await message.reply_text("Hello, i am test bot!")


#run the bot
if __name__ == '__main__':
    bot.run()
#bot.start()
#print("started")
#idle()
