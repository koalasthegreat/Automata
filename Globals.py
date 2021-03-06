import os

import motor.motor_asyncio
import sentry_sdk

DISABLED_PLUGINS = os.getenv("AUTOMATA_DISABLED_PLUGINS", "").split(",")

PRIMARY_GUILD = int(os.getenv("AUTOMATA_PRIMARY_GUILD", 514110851016556567))
VERIFIED_ROLE = int(os.getenv("AUTOMATA_VERIFIED_ROLE", 564672793380388873))

WHITELIST_HTTP_API_BEARER_TOKEN = os.getenv("WHITELIST_HTTP_API_BEARER_TOKEN", None)

MONGO_HOST = os.getenv("AUTOMATA_MONGO_HOST", "mongo")
MONGO_ADDRESS = f"mongodb://{MONGO_HOST}/automata"

DISCORD_AUTH_URI = os.getenv("DISCORD_AUTH_URI", "https://discord.muncompsci.ca")

mongo_client = motor.motor_asyncio.AsyncIOMotorClient(MONGO_ADDRESS)

if os.getenv("SENTRY_DSN", None):
    sentry_sdk.init(os.environ["SENTRY_DSN"])
