import discord
henk = {
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
            "genshin": "gayshitInfect"
        },
        "phase": "voting"
    }
}

async def vote(interaction, gameName, points, chosenPoll):
    if points < 4 and points > 0:
        await interaction.response.send_message(f"<@{interaction.user.id}> picked the game {gameName} for {points} points, in the poll {chosenPoll}.")
    else:
        await interaction.response.send_message(content="Invalid number, you can only pick a number between 1 and 3.", ephemeral=True)