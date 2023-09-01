import uuid
import discord
import data_handling 

# emiels code start hier

async def add_reference(interaction: discord.Interaction, keyword, replacement):
    if data_handling.user_is_admin(interaction):
        data = data_handling.getData()
        if str(interaction.guild_id) in data:
            if keyword != replacement:
                data[str(interaction.guild_id)]["reference"][str(keyword).lower()] = str(replacement)
                await interaction.response.send_message(f"**`{keyword}`** will now be replaced with **`{replacement}`**!", ephemeral=True)
                data_handling.saveData(data)
            else:
                await interaction.response.send_message("Hey there buddy, the reference cannot be the same as the replacement :wink:", ephemeral=True)

async def remove_reference(interaction: discord.Interaction, keyword, replacement):
    print()

async def display_references(interaction: discord.Interaction, keyword, replacement):
    print()
# emiels code eindigt hier

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
