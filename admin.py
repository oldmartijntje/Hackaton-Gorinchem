import uuid
import discord
import data_handling 

# emiels code start hier
import random

deniedList = ["https://tenor.com/view/request-denied-colonel-sharp-gi-joe-a-real-american-hero-the-synthoid-conspiracy-deny-gif-17529846", "https://tenor.com/view/nope-gif-18506271", "https://tenor.com/view/no-way-dude-no-oh-bugs-bunny-bugs-gif-22941840", "https://tenor.com/view/smg4-mission-failed-successfully-mission-failed-mario-luigi-gif-26027979", "You don't have admin permissions."]
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
        else:
            await interaction.response.send_message("This server is not yet registered, register it by creating a poll.")
    else:
        await interaction.response.send_message(random.choice(deniedList))

async def remove_reference(interaction: discord.Interaction, keyword):
    if data_handling.user_is_admin(interaction):
        data = data_handling.getData()
        if str(interaction.guild_id) in data:
            if str(keyword).lower() in data[str(interaction.guild_id)]["reference"]:
                data[str(interaction.guild_id)]["reference"].pop(str(keyword).lower())
                data_handling.saveData(data)
                await interaction.response.send_message(f"**{keyword}** has succesfully been unlinked! \nhttps://tenor.com/view/thanos-infinity-gauntlet-snap-finger-snap-gif-12502580", ephemeral=True)
            else:
                await interaction.response.send_message(f"{keyword} is not a valid reference, check if you made any typos and try again.", ephemeral=True)
        else:
            await interaction.response.send_message("This server does not have any references.")
    else:
        await interaction.response.send_message(random.choice(deniedList))

async def display_references(interaction: discord.Interaction):
    data = data_handling.getData()
    references = list(data[str(interaction.guild_id)]["reference"].keys())
    response = "List of references:\n"
    for item in references:
        response = f"{response}- **{str(item)}** = **{data[str(interaction.guild_id)]['reference'][str(item)]}**\n"
    await interaction.response.send_message(response, ephemeral=True)
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
