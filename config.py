import os
from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")

# mpd config
host = os.getenv("HOST")
port = int(os.getenv("PORT"))
timeout = int(os.getenv("TIMEOUT"))
idleTimeout = None
