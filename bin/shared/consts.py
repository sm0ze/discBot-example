import os
import socket
import time

import bin.log as log

logP = log.get_logger(__name__)


# function to grab a discord bot token
# from user if one is not found in the .env
def askToken(var: str) -> str:
    tempToken = input(f"Enter your {var}: ")
    with open(".env", "a+") as j:
        j.write(f"{var}={tempToken}\n")
    return tempToken


CMD_PREFIX = "-"
START_TIME = time.time()

HOST_NAME = socket.gethostname().lower()
logP.info(f"Name of host for program is: {HOST_NAME}")
logP.info(f"Saving logs at: {log.LOG_FILE}")


TOKEN = os.getenv("DISCORD_TOKEN")

if not TOKEN:
    logP.warning("No Discord Token")
    TOKEN = askToken("DISCORD_TOKEN")
