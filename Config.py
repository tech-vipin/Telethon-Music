import os

class Config(object):
    API_ID = int(os.environ.get("APP_ID", "20879666"))
    API_HASH = os.environ.get("API_HASH", "bad13c21c74240c60e1820fee35923c2")
    BOT_TOKEN = os.environ.get("BOT_TOKEN", "6761553201:AAHUqredKvOv1kjZ38vG8Lyc7j16TGn0-9k")
    STRING_SESSION = os.environ.get("STRING_SESSION", "BQCkbowLfQ2dy3625z32sd82n_nxKvGjikUTic-WGpuJYEyXO43p1klC3kizfK6UIyRbSThAYaRuySp83JI8PkUJmuuqHC1U69-N8zQdntSZo0eamPDR-O8giHqiBMjw7J6IoPZkAGi2SICWLW769fZCiSjCKkShfUW6e6yuEOvtwHXY0-yZhLSi-9LcDqGlSYoOhLl4_fV78eKldET1brCcvZEISfcEqQJy4-jk9SIZlwFTPIxpXeeKf75CFq1PEsljtQu9lMxw_URwvuyMHgXuR8Y_6Co4LAdNaJ-mAQZP-DzNaAr54FhaYy2IKMn2rCpmz90untVUoP8yGmFcnWfnAAAAAYYlMwEA")
    MANAGEMENT_MODE = os.environ.get("MANAGEMENT_MODE", True)
    HEROKU_MODE = os.environ.get("HEROKU_MODE", None)
    BOT_USERNAME = os.environ.get("BOT_USERNAME", "BitklyMusicBot")
    SUPPORT = os.environ.get("SUPPORT", "TheSupportChat") # Your Support
    CHANNEL = os.environ.get("CHANNEL", "TheUpdatesChannel") # Your Channel
    START_IMG = os.environ.get("START_IMG", "https://telegra.ph/file/4c90284c76220d779899b.png")
    CMD_IMG = os.environ.get("CMD_IMG", "https://telegra.ph/file/4c90284c76220d779899b.png")
    ASSISTANT_ID = int(os.environ.get("ASSISTANT_ID", "6545552129")) # telegram I'd not Username
    AUTO_LEAVE_TIME = int(os.environ.get("AUTO_LEAVE_ASSISTANT_TIME", "54000")) # in seconds
    AUTO_LEAVE = os.environ.get('AUTO_LEAVING_ASSISTANT', None) # Change it to "True"
