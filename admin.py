import uuid
import discord
import data_handling 

async def test(interaction: discord.Interaction, vote_name): 
    if vote_name == '':
        vote_name = str(uuid.uuid4())
    if data_handling.user_is_admin(interaction):
        print(data_handling.addPollToData(interaction, vote_name))
    await interaction.response.send_message(vote_name)