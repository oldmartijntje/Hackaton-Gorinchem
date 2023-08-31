import uuid
import discord
import data_handling 

async def test(interaction: discord.Interaction, vote_name): 
    if vote_name == '':
        vote_name = str(uuid.uuid4())
    if data_handling.user_is_admin(interaction):
        if data_handling.addPollToData(interaction, vote_name):
            await interaction.response.send_message(f"Succesfully created poll {vote_name}!")
        else:
            await interaction.response.send_message(f"The poll {vote_name} already exists!")
    else:
        await interaction.response.send_message(f"You don't have the rights to create a poll!")