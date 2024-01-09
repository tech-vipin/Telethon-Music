import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "20879666"))
    API_HASH = os.environ.get("API_HASH", "bad13c21c74240c60e1820fee35923c2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "")
    STRING_SESSION = os.environ.get("STRING_SESSION", "")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", True)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://te.legra.ph/file/7f1312799ebb3d7e75bb5.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://te.legra.ph/file/7f1312799ebb3d7e75bb5.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6545552129")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "120000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', Tru±e) # Change it to "True"
