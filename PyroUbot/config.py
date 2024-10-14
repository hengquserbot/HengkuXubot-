import os

API_ID = int(os.getenv("API_ID", "22016511"))
API_HASH = os.getenv("API_HASH", "8267335b1cbd700a179dbe9a9a482d1e")
BOT_TOKEN = os.getenv("BOT_TOKEN", "7498928789:AAGn8R-TqA98cIK--9pQQnMHkkPMI_r0lzw")
OWNER_ID = int(os.getenv("OWNER_ID", "1846313396"))
LOGS_MAKER_UBOT = int(os.getenv("LOGS_MAKER_UBOT", "-1002448404141"))
BLACKLIST_CHAT = list(map(int, os.getenv("BLACKLIST_CHAT", "-1002109872719 -1002058863067 -1001986858575 -1001287188817 -1002226843410").split()))
MAX_BOT = int(os.getenv("MAX_BOT", "100"))
RMBG_API = os.getenv("RMBG_API", "b5ZnjZ2nUUpbdEHfcrWdjWbC")
AI_GOOGLE_API = os.getenv("AI_GOOGLE_API", "AIzaSyAM4A7L0Qj3loDZDupt0X74PDne6Tx2YLA")
MONGO_URL = os.getenv(
    "MONGO_URL",
    "mongodb+srv://Japran:memek@cluster0.bvzu1.mongodb.net/?retryWrites=true&w=majority&appName=Cluster0",
)
START_IMG_URL = os.getenv(
    "START_IMG_URL", "https://itzpire.com/file/93496dbb7582.jpg"
)

DEVS = [
    6953052196, #devsganteng
    1846313396
]
