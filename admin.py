import discord

async def test(interaction: discord.Interaction, vote_name): 
    if vote_name == '':
        vote_name = "aaaaaa"
    await interaction.response.send_message(vote_name)