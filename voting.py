import discord
import json

async def vote(interaction, gameName, points, chosenPoll):
    with open("data.json", "r") as dataList:
        dataList = json.loads(dataList.read())
    if interaction.guild_id in dataList:
        if gameName in dataList[f"{interaction.guild_id}"]["reference"]:
            gameName = dataList[f"{interaction.guild_id}"]["reference"][gameName]
        if points < 4 and points > 0:
            with open("data.json", "w") as data:
                if points > 1:
                    await interaction.response.send_message(f"<@{interaction.user.id}> Successfully voted for **{gameName}** for **{points}** points, in **{chosenPoll}**.", ephemeral=True)
                else:
                    await interaction.response.send_message(f"<@{interaction.user.id}> Successfully voted for **{gameName}** for **{points}** point, in **{chosenPoll}**.", ephemeral=True)
        else:
            await interaction.response.send_message(content="Invalid number, you can only pick a number between **1** and **3**.", ephemeral=True)
    else:
        interaction.response.send_message("This server has not yet started a poll, please create one first.")