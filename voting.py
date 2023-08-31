import json
import data_handling
import discord

async def vote(interaction: discord.Interaction, gameName, points, chosenPoll):
    dataDict = data_handling.getData()
    if str(interaction.guild_id) in dataDict:
        if gameName.lower() in dataDict[f"{interaction.guild_id}"]["reference"]:
            gameName = dataDict[f"{interaction.guild_id}"]["reference"][gameName]
        if points < 4 and points > 0:
            if chosenPoll in dataDict[f"{interaction.guild_id}"]["polls"]:
                data = data_handling.getData()
                poll = data[str(interaction.guild_id)]["polls"][chosenPoll]
                votes = poll["votes"]
                if poll["phase"] == "adding":
                    if gameName not in poll["gameList"]:
                        poll["gameList"].append(gameName)
                    await addVotingToUserAndGiveFeedback(interaction, votes, gameName, points, chosenPoll)
                elif poll["phase"] == "voting":
                    if gameName in poll["gameList"]:
                        await addVotingToUserAndGiveFeedback(interaction, votes, gameName, points, chosenPoll)
                    else:
                        await interaction.response.send_message(f"Sorry <@{interaction.user.id}>, but {gameName}, is not a valid option for this poll.")
                elif poll["phase"] == "closed":
                    await interaction.response.send_message(f"Sorry <@{interaction.user.id}>, but voting on this poll has already been finished.")
                
                if not str(interaction.user.name) in votes:
                    votes[interaction.user.name] = {"1points": "", "2points": "", "3points": ""}

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


async def addVotingToUserAndGiveFeedback(interaction: discord.Integration, votes, gameName, points, chosenPoll):
    votes = checkDuplicateGames(interaction, votes, gameName)
    if not str(interaction.user.name) in votes:
        votes[interaction.user.name] = {"1points": "", "2points": "", "3points": ""}
    if votes[interaction.user.name][f"{points}points"] != "":
        votes = checkBeforeReplacing(interaction, votes, points)
    votes[interaction.user.name][f"{points}points"] = gameName
    if points > 1:
        await interaction.response.send_message(f"<@{interaction.user.id}> Successfully voted for **{gameName}** for **{points}** points, in **{chosenPoll}**.", ephemeral=True)
    else:
        await interaction.response.send_message(f"<@{interaction.user.id}> Successfully voted for **{gameName}** for **{points}** point, in **{chosenPoll}**.", ephemeral=True)

def checkBeforeReplacing(interaction: discord.Integration, votes, points):
    if points > 1 and votes[interaction.user.name][f"{points-1}points"] == "":
        votes[interaction.user.name][f"{points-1}points"] = votes[interaction.user.name][f"{points}points"]
    elif points > 2 and votes[interaction.user.name][f"{points-2}points"] == "":
        votes[interaction.user.name][f"{points-2}points"] = votes[interaction.user.name][f"{points}points"]
    return votes

def checkDuplicateGames(interaction: discord.Integration, votes, gameName):
    for item in list(votes[interaction.user.name].keys()):
        if votes[interaction.user.name][item] == gameName:
            votes[interaction.user.name][item] = ""
    return votes

async def getMyVotes(interaction: discord.Interaction, chosenPoll):
    pass