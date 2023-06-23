import disnake
from disnake.ext import commands

from config import config


class Bot(commands.InteractionBot):
    async def on_ready(self):
        activity_text = "Text"
        activity_type = disnake.ActivityType.playing
        activity = disnake.Activity(type=activity_type, name=activity_text)

        await self.change_presence(activity=activity)

        print("System: Bot started!")


def main():
    bot = Bot()
    bot.run(config["bot_token"])


if __name__ == "__main__":
    main()
