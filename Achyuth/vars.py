import os
from os import getenv, environ
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    MULTI_CLIENT = True
    API_ID = int(getenv('API_ID','')) #Get It From my.telegram.org
    API_HASH = str(getenv('API_HASH','')) #Get It From my.telegram.org
    BOT_TOKEN = str(getenv('BOT_TOKEN','')) #Get It From @BotFather
    name = str(getenv('name', 'Achyuth'))
    SLEEP_THRESHOLD = int(getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(getenv('WORKERS', '4'))
    BIN_CHANNEL = int(getenv('BIN_CHANNEL', '')) #Where all files stored at a place
    PORT = int(getenv('PORT', 8080))
    BIND_ADRESS = str(getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0'))
    PING_INTERVAL = int(environ.get("PING_INTERVAL", "1200"))  # 20 minutes
    OWNER_ID = set(int(x) for x in os.environ.get("OWNER_ID", "").split()) #Give Owner Id
    NO_PORT = bool(getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = str(getenv('OWNER_USERNAME','')) #Username Of Bot Owner
    if 'DYNO' in environ:
        ON_HEROKU = True
        APP_NAME = str(getenv('APP_NAME', 'Achyuth'))
    
    else:
        ON_HEROKU = False
    ON_HEROKU = True
    FQDN = (getenv('FQDN', '')) if not ON_HEROKU or getenv('FQDN','') else APP_NAME+'.herokuapp.com'
    HAS_SSL=bool(getenv('HAS_SSL',True))
    if HAS_SSL:
        URL = "https://{}/".format(FQDN)
    else:
        URL = "http://{}/".format(FQDN)
    DATABASE_URL = str(getenv('DATABASE_URL','')) #Usr MongoDb
    UPDATES_CHANNEL = str(getenv('UPDATES_CHANNEL', '')) #Give Updates Channel Which Is Used For ForceSub.Channel Must Be Public And Make Bot As Admin In Channel 
    BANNED_CHANNELS = list(set(int(x) for x in str(getenv("BANNED_CHANNELS", "")).split()))
    
