import asyncio
import discord
from discord.ext import commands

from pretty_help import DefaultMenu, PrettyHelp
import bin.log as log
from bin.shared.consts import (
    CMD_PREFIX,
    HOST_NAME,
    START_TIME,
    TOKEN,
)


logP = log.get_logger(__name__)

runBot = True
cogList: list[str] = ["commands.exampleCog.py"]

logP.info(
    f"Bot will attempt to connect to discord on host: {HOST_NAME}, {runBot}"
)


logP.debug(f"Bot start time set as: {START_TIME}")


INTENTS = discord.Intents.default()
SYNC = False


class myBot(commands.Bot):
    async def setup_hook(self):
        logP.info("Bot has logged in...")
        if SYNC:
            await asyncio.sleep(5)
            commandList = await self.tree.sync()
            logP.debug(f"Sync commands: {commandList}")


menu = DefaultMenu(
    page_left="⬅️",
    page_right="➡️",
    remove="⏹️",
    active_time=60,
)
ending_note = "{ctx.bot.user.name}"


bot = myBot(
    command_prefix=CMD_PREFIX,
    case_insensitive=True,
    intents=INTENTS,
)

bot.help_command = PrettyHelp(
    menu=menu,
    ending_note=ending_note,
    delete_after_timeout=True,
    no_category="Basic Commands",
    index_title="Command Lists",
)


async def load_extensions():
    for filename in cogList:
        if filename.endswith(".py"):
            logP.debug(f"Loading Cog: {filename}")
            await bot.load_extension(f"bin.{filename[:-3]}")

        # general exception for excluding __pycache__
        # while accounting for generation of other filetypes
        elif filename.endswith("__"):
            continue
        else:
            print(f"Unable to load {filename[:-3]}")


async def main():
    async with bot:

        # discord.py cog importing
        await load_extensions()

        # and to finish. run the bot
        if runBot:
            logP.info("Bot connection starting....")
            await bot.start(TOKEN, reconnect=True)


# general import protection
if __name__ == "__main__":
    asyncio.run(main())

logP.critical("Bot has reached end of file")
