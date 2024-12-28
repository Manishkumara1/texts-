import os

API_ID    = os.environ.get("API_ID", "21537501")
API_HASH  = os.environ.get("API_HASH", "02d8ef0eae2926ec4fd0cbff05ec0737")
BOT_TOKEN = os.environ.get("BOT_TOKEN", "7451364068:AAHuhmL_f1XsLkMOSIIJSeGCIVB7_fqmicM") 

WEBHOOK = True  # Don't change this
PORT = int(os.environ.get("PORT", 8080))  # Default to 8000 if not set
