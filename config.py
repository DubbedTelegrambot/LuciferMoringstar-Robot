import re
from os import environ
from translation import LuciferMoringstar
id_pattern = re.compile(r'^.\d+$')
def is_enabled(value, default):
    if value.lower() in ["true", "yes", "1", "enable", "on"]:
        return True
    elif value.lower() in ["false", "no", "0", "disable", "off"]:
        return False
    else:
        return default

# ==================================
API_ID = int(environ["API_ID"])
API_HASH = environ["API_HASH"]
B_KEYS = environ["BOT_TOKEN"]
START_MSG = environ.get("START_MSG", LuciferMoringstar.DEFAULT_MSG)
BOT_PICS = (environ.get('BOT_PICS', "https://telegra.ph/file/9e1e73d9b15cc16fe0e99.jpg https://telegra.ph/file/86a5d907ff6121f5bbbc9.jpg https://telegra.ph/file/c71fdc2346e179944a071.jpg https://telegra.ph/file/440c2ec85ce7862c4cf02.jpg https://telegra.ph/file/b31d72c3eb0373d791250.jpg https://telegra.ph/file/e07ea4327171c6b76ec0e.jpg https://telegra.ph/file/e49c27a9f2ca6368b3fcb.jpg")).split()
SUPPORT = environ.get("SUPPORT", "t.me/Mo_Tech_YT")
LOG_CHANNEL = int(environ.get("LOG_CHANNEL", None))
DATABASE_URI = environ.get("DATABASE_URI", None)
FORCE = environ.get('FORCES_SUB')
CUSTOM_FILE_CAPTION = environ.get("CUSTOM_FILE_CAPTION", LuciferMoringstar.FILE_CAPTIONS)
DEV_NAME = environ.get("DEV_NAME", "Muhammed")
ADMINS = [int(admin) if id_pattern.search(admin) else admin for admin in environ['ADMINS'].split()]
CHANNELS = [int(ch) if id_pattern.search(ch) else ch for ch in environ['CHANNELS'].split()]
AUTH_GROUPS = [int(admin) for admin in environ.get("AUTH_GROUPS", "").split()]
auth_users = [int(user) if id_pattern.search(user) else user for user in environ.get('AUTH_USERS', '').split()]


# ==================================
# Empty 😂
COLLECTION_NAME = environ.get('COLLECTION_NAME', 'Telegram_files')
CACHE_TIME = int(environ.get('CACHE_TIME', 300))
USE_CAPTION_FILTER = bool(environ.get('USE_CAPTION_FILTER', False))
BUTTONS = {}
CURRENT = int(environ.get("SKIP", 2))
CANCEL = False
FORCES_SUB = int(FORCE) if FORCE and id_pattern.search(FORCE) else FORCE
DATABASE_NAME = environ.get("DATABASE_NAME", 'Gofilefhjrobot')
AUTH_USERS = (auth_users + ADMINS) if auth_users else []
# ==================================
# About Bot 🤖
class bot_info(object):
    BOT_NAME = None
    BOT_USERNAME = None
    BOT_ID = None


