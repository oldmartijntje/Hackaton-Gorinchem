import json
import data_handling

async def vote(interaction, gameName, points, chosenPoll):
    with open("data.json", "r") as dataList:
        dataList = json.loads(dataList.read())
    if str(interaction.guild_id) in dataList:
        if gameName in dataList[f"{interaction.guild_id}"]["reference"]:
            gameName = dataList[f"{interaction.guild_id}"]["reference"][gameName]
        if points < 4 and points > 0:
            if chosenPoll in dataList[f"{interaction.guild_id}"]["polls"]:
                data = data_handling.getData()
                if points > 1:
                    await interaction.response.send_message(f"<@{interaction.user.id}> Successfully voted for **{gameName}** for **{points}** points, in **{chosenPoll}**.", ephemeral=True)
                else:
                    await interaction.response.send_message(f"<@{interaction.user.id}> Successfully voted for **{gameName}** for **{points}** point, in **{chosenPoll}**.", ephemeral=True)
                poll = data[str(interaction.guild_id)]["polls"][chosenPoll]
                votes = poll["votes"]
                if not str(interaction.user.name) in votes:
                    votes[interaction.user.name] = {"1point": "", "2points": "", "3points": ""}

                if points == 1:
                    votes[interaction.user.name]["1point"] = gameName
                elif points == 2:
                    votes[interaction.user.name]["2points"] = gameName
                else:
                    votes[interaction.user.name]["3points"] = gameName

                data_handling.saveData(data)
            else:
                await interaction.response.send_message(f"<@{interaction.user.id}> This poll does not exist, check if you made a typo and try again ;)", ephemeral=True)
        else:
            if points == 69 or gameName == "69" or chosenPoll == "69":
                await interaction.response.send_message("https://tenor.com/view/linus-you-funny-gif-21112056", ephemeral=True)
            else:
                await interaction.response.send_message(content="Invalid number, you can only pick a number between **1** and **3**.", ephemeral=True)
    else:
        await interaction.response.send_message("This server has not yet started a poll, please create one first.", ephemeral=True)