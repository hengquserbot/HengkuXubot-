import os

API_ID = int(os.getenv("API_ID", "17855094"))
API_HASH = os.getenv("API_HASH", "004a12ddadfd7e96afa84af7f37e4fe6")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7498928789:7408701168:AAHcOTjV2ob4AvqWW5VNZHa72N6oHIbZEPk")
OWNER_ID = int(os.getenv("OWNER_ID", "17855094"))
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "--1002369567634"))
BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002109872719 ").split()))
MAX_BOT = int(os.getenv("MAX_BOT", "100"))
RMBG_API = os.getenv("RMBG_API", "b5ZnjZ2nUUpbdEHfcrWdjWbC")
AI_GOOGLE_API = os.getenv("AI_GOOGLE_API", "#AIzaSyAM4A7L0Qj3loDZDupt0X74PDne6Tx2YLA")
MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://ceyycantik05xlmghbnj@cluster0.t2jqp.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
START_IMG_URL = os.getenv(
    "START_IMG_URL", "https://itzpire.com/file/93496dbb7582.jpg"
)

DEVS = [
    17855094, #devscool
]
