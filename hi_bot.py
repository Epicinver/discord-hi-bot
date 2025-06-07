import discord
from discord.ext import commands

intents = discord.Intents.default()
intents.message_content = True  # Enable to read message content

bot = commands.Bot(command_prefix="!", intents=intents)

@bot.event
async def on_ready():
    print(f"Logged in as {bot.user}")

@bot.event
async def on_message(message):
    # Prevent the bot from replying to itself
    if message.author == bot.user:
        return

    # Check if "hi" appears anywhere in the message (case insensitive)
    if "hi" in message.content.lower():
        await message.channel.send(f"Hi, {message.author.mention}!")

    # Process other commands if you add any later
    await bot.process_commands(message)

bot.run("Put your token here, this originally was my code, but GitHub told me that this has my bot token.")