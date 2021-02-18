import os

LOG_LEVEL = os.getenv("LOG_LEVEL", "DEBUG")
TELEGRAM_BOT_TOKEN = os.environ["TELEGRAM_BOT_TOKEN"]
TELEGRAM_PROXY_SETTINGS = {}
if "TELEGRAM_PROXY_URL" == os.environ:
    TELEGRAM_PROXY_SETTINGS = {
        "proxy_url": os.environ["TELEGRAM_PROXY_URL"],
        "urllib3_proxy_kwargs": {
            "username": os.environ["TELEGRAM_PROXY_LOGIN"],
            "password": os.environ["TELEGRAM_PROXY_PASSWORD"],
        },
    }
