#Github.com/Vasusen-code

from pyrogram import Client

from telethon.sessions import StringSession
from telethon.sync import TelegramClient

from decouple import config
import logging, time, sys

logging.basicConfig(format='[%(levelname) 5s/%(asctime)s] %(name)s: %(message)s',
                    level=logging.WARNING)

# variables
API_ID = config("API_ID", default=12099140, cast=int)
API_HASH = config("API_HASH", default="1740646db2628dabd953712e45b044a1")
BOT_TOKEN = config("BOT_TOKEN", default="6549391784:AAF630wJgDxp-YetbMOsWd8EBj8yDgaqusk")
SESSION = config("SESSION", default="BQCxIhWVjtIsKpbWuvVeCABPEdGgMPNmPVmdc7FCl-kn5P4f0aTgVmuSdHL5IPkf7378ykmdBTbqLiFg_TnHS4jl-D6g2T50_VoQrdUVu4x2v-d2A_3Ii51W8rP1nXuo9UDXSBHhFEzW5uVyIEGD24VWBCIO5lM3S0TMDLPAfd4fbpXanvSeLila0Z8sc_kWpx-zzmld8Y15-KfbIBXBDlW5nV-kXg39FePy0SrI2nSRTTi1PXGtnj6neSdvK4nHZlLw1SmkFc4O5T1Gsdzg1N4W3Dm9CDxHjAuUXDo9IFgblIHb1SDaee4CqCsWXway6kASettDr9mABF8B2sQ_4iUaAAAAATgvoVIA")
FORCESUB = config("FORCESUB", default="Pantham_Malayalam")
AUTH = config("AUTH", default=5237612882, cast=int)

bot = TelegramClient('bot', API_ID, API_HASH).start(bot_token=BOT_TOKEN) 

userbot = Client("saverestricted", session_string=SESSION, api_hash=API_HASH, api_id=API_ID) 

try:
    userbot.start()
except BaseException:
    print("Userbot Error ! Have you added SESSION while deploying??")
    sys.exit(1)

Bot = Client(
    "SaveRestricted",
    bot_token=BOT_TOKEN,
    api_id=int(API_ID),
    api_hash=API_HASH
)    

try:
    Bot.start()
except Exception as e:
    print(e)
    sys.exit(1)
