import os
from typing import final
from dotenv import load_dotenv
load_dotenv(dotenv_path="./.env")

# mpd config
host: final = os.getenv("HOST")
port: final = int(os.getenv("PORT"))
timeout: final = int(os.getenv("TIMEOUT"))
idleTimeout: final = None
