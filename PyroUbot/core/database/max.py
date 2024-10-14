from PyroUbot.core.database import mongodb 

aktif = mongodb["PyroUbot"]["uptime"]


async def get_uptime(user_id):
    user = await aktif.users.find_one({"_id": user_id})
    if user:
        return user.get("uptime")
    else:
        return None


async def set_uptime(user_id, expire_date):
    await aktif.users.update_one(
        {"_id": user_id}, {"$set": {"uptime": expire_date}}, upsert=True
    )


async def rem_uptime(user_id):
    await aktif.users.update_one(
        {"_id": user_id}, {"$unset": {"uptime": ""}}, upsert=True
    )