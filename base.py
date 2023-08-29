import discord
from discord.ext import commands
from discord import app_commands
import admin

bot = commands.Bot(command_prefix="uno!", intents = discord.Intents.all())

keyFile = open("secrets.txt", "r")
key = keyFile.read()

@bot.event
async def on_ready():
    print(f'We have logged in as {bot.user}')
    print("bot is Up and Ready!")
    try:
        synced = await bot.tree.sync()
        print(f"Synched {len(synced)} command(s)")
    except Exception as e:
        print(e)
    

@bot.event
async def on_message(message):
    if message.author == bot.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello World!')

# make the slash command
@bot.tree.command(name="say")
@app_commands.describe(thing_to_say = "what should i say?")
async def slash_command(interaction: discord.Interaction, thing_to_say: str):    
    await interaction.response.send_message(thing_to_say)

@bot.tree.command(name="start_vote")
@app_commands.describe(vote_name = "What is the name of the vote?")
async def startVote(interaction: discord.Interaction, vote_name: str = ''):  
    print(interaction.user.guild_permissions.administrator)
    await admin.test(interaction, vote_name)

bot.run(token=key)