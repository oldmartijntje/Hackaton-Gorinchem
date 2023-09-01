import discord

intents = discord.Intents.default()
intents.message_content = True

client = discord.Client(intents=intents)

keyFile = open("secrets.txt", "r")
key = keyFile.read()

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    if message.content.startswith('$hello'):
        await message.channel.send('Hello World!')

@bot.tree.command(name="say", description="Copies your text")
@app_commands.describe(thing_to_say = "what should i say?")
async def say(interaction: discord.Interaction, thing_to_say: str):    
    await interaction.response.send_message(thing_to_say)

@bot.tree.command(name="vote", description="Bring out your vote on a poll")
@app_commands.describe(poll = "poll", vote = "game", score = "your points")
async def vote(interaction: discord.Interaction, vote: str, score:int, poll:str):
    await voting.vote(interaction, gameName=vote, points=score, chosenPoll=poll)

@bot.tree.command(name="get_votes", description="See what you have voted for on a specific poll or server")
@app_commands.describe(chosen_poll = "The poll you want to inspect.")
async def get_votes(interaction: discord.Interaction, chosen_poll: str = ""):
    await voting.getMyVotes(interaction, chosen_poll)
    
@bot.tree.command(name="test_data_handling", description="Testing data handling functions")
@app_commands.describe(thing_to_say="what should i say?")
async def test_data_handling(interaction: discord.Interaction, thing_to_say: str):
    print(data_handling.user_is_admin(interaction))
    await interaction.response.send_message(thing_to_say)
    
@bot.tree.command(name="start_poll", description="Start a poll.")
@app_commands.describe(vote_name = "What is the name of the vote?")
async def startVote(interaction: discord.Interaction, vote_name: str = ''):  
    await admin.test(interaction, vote_name)

@bot.tree.command(name="get_poll_list", description="Get a list of all active polls")
async def get_poll_list(interaction: discord.Interaction):
    poll_list = data_handling.get_poll_list(interaction)
    await interaction.response.send_message(poll_list)

bot.run(token=key)