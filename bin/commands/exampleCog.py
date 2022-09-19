import typing
import discord
from discord.ext import commands


class defaultCommands(
    commands.Cog,
    name="Default Commands",
    description="Default Desciption",
):
    def __init__(
        self, bot: typing.Union[commands.bot.Bot, commands.bot.AutoShardedBot]
    ):
        self.bot = bot

    @discord.app_commands.command(
        name="ping",
        description="Ping...",
    )
    async def change_stat(
        self,
        inter: discord.Interaction,
    ):
        await inter.response.send_message("...Pong", ephemeral=True)


async def setup(bot: commands.Bot):
    await bot.add_cog(defaultCommands(bot))
