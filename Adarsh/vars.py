import os
from dotenv import load_dotenv

load_dotenv()

class Var(object):
    MULTI_CLIENT = False
    API_ID = int(os.getenv('API_ID', '25198711'))  # Corrected to use os.getenv instead of getenv
    API_HASH = os.getenv('API_HASH', '2a99a1375e26295626c04b4606f72752')  # Corrected to use os.getenv
    BOT_TOKEN = os.getenv('BOT_TOKEN', '')  # Bot token should ideally be securely handled
    name = os.getenv('name', 'robot')
    SLEEP_THRESHOLD = int(os.getenv('SLEEP_THRESHOLD', '60'))
    WORKERS = int(os.getenv('WORKERS', '4'))
    BIN_CHANNEL = int(os.getenv('BIN_CHANNEL', '-1002151954601'))
    PORT = int(os.getenv('PORT', '8080'))
    BIND_ADDRESS = os.getenv('WEB_SERVER_BIND_ADDRESS', '0.0.0.0')  # Corrected BIND_ADDRESS
    PING_INTERVAL = int(os.getenv("PING_INTERVAL", "1200"))  # Corrected to use os.getenv
    OWNER_ID = set(int(x) for x in os.getenv("OWNER_ID", "1002151954601").split())  # Corrected to use os.getenv and set conversion
    NO_PORT = bool(os.getenv('NO_PORT', False))
    APP_NAME = None
    OWNER_USERNAME = os.getenv('OWNER_USERNAME', 'ANIFLIX')
    
    if 'DYNO' in os.environ:
        ON_HEROKU = True
        APP_NAME = os.getenv('APP_NAME')  # Corrected to use os.getenv
    else:
        ON_HEROKU = False
    
    FQDN = os.getenv('FQDN', BIND_ADDRESS) if not ON_HEROKU or os.getenv('FQDN') else APP_NAME + '.herokuapp.com'
    HAS_SSL = bool(os.getenv('HAS_SSL', False))
    
    if HAS_SSL:
        URL = f"https://{FQDN}/"  # Using f-string for URL formatting
    else:
        URL = f"http://{FQDN}/"  # Using f-string for URL formatting
    
    DATABASE_URL = os.getenv('DATABASE_URL', 'mongodb+srv://Aniflix:Lipun123@aniflix.q2wina5.mongodb.net/?retryWrites=true&w=majority&appName=Aniflix')
    UPDATES_CHANNEL = os.getenv('UPDATES_CHANNEL', 'Aniflix_Official')
    BANNED_CHANNELS = list(set(int(x) for x in os.getenv("BANNED_CHANNELS", "-1001362659779").split()))  # Corrected to use os.getenv and set conversion
