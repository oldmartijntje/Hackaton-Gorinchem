import discord
from discord.ext import commands
from discord import app_commands
import voting
import data_handling
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

@bot.tree.command(name="say", description="Copies your text")
@app_commands.describe(thing_to_say = "what should i say?")
async def say(interaction: discord.Interaction, thing_to_say: str):
    print(thing_to_say)
    await interaction.response.send_message(thing_to_say)

@bot.tree.command(name="vote", description="Bring out your vote on a poll")
@app_commands.describe(poll = "poll", vote = "game", score = "your points")
async def vote(interaction: discord.Interaction, vote: str, poll:str, score:int=3):
    await voting.vote(interaction, gameName=vote, points=score, chosenPoll=poll)

@bot.tree.command(name="get_votes", description="See what you have voted for on a specific poll or server")
@app_commands.describe(chosen_poll = "The poll you want to inspect.")
async def get_votes(interaction: discord.Interaction, chosen_poll: str = ""):
    await voting.getMyVotes(interaction, chosen_poll)
    
# martijns code start hier
@bot.tree.command(name="close_poll", description="Finish the poll and get the results.")
@app_commands.describe(poll = "Poll name")
async def close_poll(interaction: discord.Interaction, poll: str):
    await admin.endPoll(interaction, poll)

@bot.tree.command(name="start_voting", description="Change it to voting phase.")
@app_commands.describe(poll = "Poll name")
async def start_voting(interaction: discord.Interaction, poll: str):
    await admin.addingPhase(interaction, poll)

# martijns code eindigt hier

@bot.tree.command(name="test_data_handling", description="Testing data handling functions")
@app_commands.describe(thing_to_say="what should i say?")
async def test_data_handling(interaction: discord.Interaction, thing_to_say: str):
    print(data_handling.user_is_admin(interaction))
    await interaction.response.send_message(thing_to_say)
    
@bot.tree.command(name="start_poll", description="Start a poll.")
@app_commands.describe(poll_name = "What is the name of the vote?")
async def startVote(interaction: discord.Interaction, poll_name: str = ''):  
    await admin.createPoll(interaction, poll_name)

# emiels code hier
@bot.tree.command(name="create_reference", description="Adds refference to the list")
@app_commands.describe(detection = "Detected word", replacement = "Replacement")
async def create(interaction: discord.Interaction, detection: str, replacement:str):
    await admin.add_reference(interaction, detection, replacement)

@bot.tree.command(name="remove_reference", description="Deletes refference from the list")
@app_commands.describe(detection = "Detected word")
async def remove(interaction: discord.Interaction, detection: str):
    await admin.remove_reference(interaction, detection)

@bot.tree.command(name="references_list", description="Shows you the list of references")
async def showList(interaction: discord.Interaction):
    await admin.display_references(interaction)

# emiels code eindigt hier

@bot.tree.command(name="get_poll_list", description="Get a list of all active polls")
async def get_poll_list(interaction: discord.Interaction):
    poll_list = data_handling.get_poll_list(interaction)
    await interaction.response.send_message(poll_list)


# jurrians code start
@bot.tree.command(name="add_admin", description="Add a user as admin to the bot")
@app_commands.describe(thing_to_say="Who do you want to give admin rights?")
async def add_admin(interaction: discord.Interaction, thing_to_say: str):
    message = data_handling.add_botadmin(interaction, thing_to_say)
    await interaction.response.send_message(message)

@bot.tree.command(name="remove_admin", description="Remove an admin from the bot")
@app_commands.describe(thing_to_say="Whose admin rights do you want to revoke?")
async def remove_admin(interaction: discord.Interaction, thing_to_say: str):
    message = data_handling.remove_botadmin(interaction, thing_to_say)
    await interaction.response.send_message(message)

@bot.tree.command(name="get_admin_list", description="See which users have admin privileges")
async def get_admin_list(interaction: discord.Interaction):
    message = data_handling.get_admin_list(interaction)
    await interaction.response.send_message(message)

@bot.tree.command(name="get_user_rights", description="See which admin rights a user has.")
async def get_user_rights(interaction: discord.Interaction, thing_to_say: str):
    condition, response = data_handling.person_rights(interaction, thing_to_say)
    if condition:
        response = f'- Server Admin: {response["server_admin"]}\n- Bot Admin: {response["bot_admin"]}'
    await interaction.response.send_message(response)

# jurrians code einde

bot.run(token=key)