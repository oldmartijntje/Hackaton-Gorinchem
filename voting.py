import discord
dataList = {
    "1041027064620388484": {
        "admins": [],
        "votes": {
            "@henkHisUserId": {
                "vote1": "minecraft",
                "vote2": "gayshitInfect",
                "vote3": "mario"
            }
        },
        "gameList": [
            "minecraft",
            "gayshitInfect",
            "mario"
        ],
        "reference": {
            "genshin": "gayshitInfect",
            "minceraft": "minecraft"
        },
        "phase": "voting"
    }
}

async def vote(interaction, gameName, points, chosenPoll):
    if gameName in dataList[f"{interaction.guild_id}"]["reference"]:
        gameName = dataList[f"{interaction.guild_id}"]["reference"][gameName]
    if points < 4 and points > 0:
        if points > 1:
            await interaction.response.send_message(f"<@{interaction.user.id}> Successfully voted for **{gameName}** for **{points}** points, in **{chosenPoll}**.", ephemeral=True)
        else:
            await interaction.response.send_message(f"<@{interaction.user.id}> Successfully voted for **{gameName}** for **{points}** point, in **{chosenPoll}**.", ephemeral=True)
    else:
        await interaction.response.send_message(content="Invalid number, you can only pick a number between **1** and **3**.", ephemeral=True)