import discord
from data_handling import DataHandling as DataHandling

async def test(interaction: discord.Interaction, vote_name): 
    if vote_name == '':
        vote_name = "aaaaaa"
    if DataHandling.user_is_admin(interaction):
        print("oui oui")
    await interaction.response.send_message(vote_name)