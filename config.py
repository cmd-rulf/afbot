from os import environ

class Config:
    API_ID = int(environ.get("API_ID", "23068471"))
    API_HASH = environ.get("API_HASH", "de232ffdec4d8b0988375398d0083a73")
    BOT_TOKEN = environ.get("BOT_TOKEN", "8217671198:AAEA_ocumXdiEAdyXVXwGQMdtZV1-h59uKc") 
    BOT_SESSION = environ.get("BOT_SESSION", "SteveBotz")
    DATABASE_URI = environ.get("DATABASE_URI", "mongodb+srv://zee:zee@cluster0.s5dgb.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0")
    DATABASE_NAME = environ.get("DATABASE_NAME", "Cluster0")
    BOT_OWNER = int(environ.get("BOT_OWNER", "5179011789"))
    
class temp(object): 
    lock = {}
    CANCEL = {}
    forwardings = 0
    BANNED_USERS = []
    IS_FRWD_CHAT = []





