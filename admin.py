import uuid
import discord

# martijns code start hier
async def endPoll(interaction: discord.Interaction, poll_name):
    if poll_name == '':
        await interaction.response.send_message(f"Needs poll name/id")
    elif data_handling.user_is_admin(interaction):
        if data_handling.doesPollExist(interaction, poll_name):
            if data[server_id]["polls"][poll_name]["phase"] == "closed":
                await interaction.response.send_message(f"This poll is already closed.")
            else:
                data = data_handling.getData()
                server_id = str(interaction.guild_id)
                data[server_id]["polls"][poll_name]["phase"] = "closed"
                data_handling.saveData(data)
                winnerDict = data_handling.calculateWinner(interaction, poll_name)
                winnerDictFormatted = data_handling.winnerDictFormatted(interaction, winnerDict)
                await interaction.response.send_message(winnerDictFormatted)
        else:
            await interaction.response.send_message(f"This poll does not exist.")
        
    else:
        await interaction.response.send_message(f"You don't have the rights to edit a poll!")
# martijns code eindigt hier

import data_handling 

async def createPoll(interaction: discord.Interaction, poll_name): 
    if poll_name == '':
        poll_name = str(uuid.uuid4())
    if data_handling.user_is_admin(interaction):
        if data_handling.addPollToData(interaction, poll_name):
            await interaction.response.send_message(f"Succesfully created poll `{poll_name}`!")
        else:
            await interaction.response.send_message(f"The poll {poll_name} already exists!")
    else:
        await interaction.response.send_message(f"You don't have the rights to create a poll!")