import discord
import data_handling 

async def test(interaction: discord.Interaction, vote_name): 
    if vote_name == '':
        vote_name = "aaaaaa"
    if data_handling.user_is_admin(interaction):
        print("oui oui")
    await interaction.response.send_message(vote_name)