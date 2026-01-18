from os import environ

class Config:
    API_ID = int(environ.get("API_ID", "25918874"))
    API_HASH = environ.get("API_HASH", "87c7c525932cf3d753bea33786ad71ee")
    BOT_TOKEN = environ.get("BOT_TOKEN", "7344124882:AAG1Y8tpX3JwzVmgyP_0jWzW_Giagzf4GsU") 
    BOT_SESSION = environ.get("BOT_SESSION", "afbot")
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://Ramzy:Ramzy@cluster0.od4yk.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER = int(environ.get("BOT_OWNER", "5179011789"))
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []


