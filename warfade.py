from pyrogram import Client, filters
import requests 
import json 
import os

TOKEN = os.environ.get("TOKEN", "")
API_ID = int(os.environ.get("API_ID",12345))
API_HASH = os.environ.get("API_HASH","")
BITLY_TOKEN = os.environ.get("BITLY_TOKEN","")

headers = {
    'Authorization': BITLY_TOKEN,
    'Content-Type': 'application/json',
}


app = Client("bitlybot" ,bot_token = TOKEN ,api_id = API_ID ,api_hash = API_HASH )

@app.on_message(filters.private & filters.command(['start']))
async def start(client,message):
  await message.reply_text(f"**Hey {message .from_user.first_name},**\n\n**Send Any Link That You Want To Shorten**\n\n_**__Made With ♥️ By @WarFade__**_", reply_to_message_id = message.message_id)
  
@app.on_message(filters.private & filters.regex("http|https"))
async def Bitly(client,message):
  URL = message.text
  DOMAIN = "bit.ly"
  value  = {'long_url': URL , 'domain': DOMAIN}
  data = json.dumps(value)
  try:
    r = requests.post('https://api-ssl.bitly.com/v4/shorten', headers=headers,data = data )
    result = r.json()
    link = result["link"]
    await message.reply_text(f"**Hey {message .from_user.first_name} , Your Shortened Url Is**\n\n{link}\n\nMade With ♥️ By @WarFade", reply_to_message_id= message.message_id)
  except Exception as e :
    await message.reply_text(e)
    
app.run()
    
