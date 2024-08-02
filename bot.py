import os
import discord
from dotenv import load_dotenv
from discord.ext import tasks
from utils import get_happy_day, get_image
from pdf_handler import save_daily_image

# Load the .env variables for the token
load_dotenv()

# Set up client
intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)

@tasks.loop(seconds=86400)
async def myLoop():
    await client.wait_until_ready()
    save_daily_image()
    for guild in client.guilds:
        channel = discord.utils.get(guild.text_channels, name='totd')
        if channel is not None:
            pinned_messages = await channel.pins()
            if len(pinned_messages) == 0:
                message = await channel.send("Greetings! I am the Theorem of the Day Bot! I send the Theorem of the Day from https://www.theoremoftheday.org to this chat for awareness and discussion.")
                await message.pin()
            await channel.send(get_happy_day(), file = discord.File("totdImage.png"))


@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')
    myLoop.start()  # Start the periodic task


if __name__ == "__main__":
    client.run(os.getenv("TOKEN"))