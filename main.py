# bot.py
import os
import discord
from dotenv import load_dotenv
from my_dir import utils

load_dotenv()
TOKEN = os.getenv('TOKEN_SPACE')
intents = discord.Intents.all()
client = discord.Client(intents=intents)


@client.event
async def on_ready():
    # Activated
    print(f'{client.user} activated!')


@client.event
async def on_message(message):
    if message.author == client.user:
        return

    # sender_id = message.author.id
    # sender_name = message.author.name
    # sender_role = message.author.roles

    message_content = message.content.lower().strip()

    if message_content == "!!help":
        await message.channel.send(f"Type '!!send invite all' to invite all users to this guild from list below:")
        for g in client.guilds:
            await message.channel.send(f"{g} ({g.id})")

    if message_content == "!!send invite all":
        await message.channel.send('As your wish.')
        try:
            for g in client.guilds:
                await utils.send_inv_all(client, g, message.guild)
        finally:
            print("error!")


client.run(TOKEN)
