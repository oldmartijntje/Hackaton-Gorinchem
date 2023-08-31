import json
import discord


def create_server(interaction: discord.Interaction):
    try:
        server_id = interaction.guild_id
        new_server_content = {
                "admins": [],
                "voteName": {
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
        with open('data.json', 'w') as servers:
            servers.write(json.dumps({server_id: new_server_content}, indent=4))
        return True
    except Exception as e:
        print(e)
        return False

def user_is_admin(interaction: discord.Interaction):
    try:
        server_id = interaction.guild_id
        user_name = interaction.user.name
        user_is_serveradmin = interaction.user.guild_permissions.administrator
        with open('data.json', 'r') as servers:
            server = json.loads(servers.read())
            admins = json.loads(servers.read())[server_id]['admins']
        user_is_botadmin = user_name in admins
        if user_is_serveradmin:
            return True
        elif user_is_botadmin:
            return True
        else:
            return False
    except Exception as e:
        print(e)
        return False


def add_botadmin(interaction: discord.Interaction):
    try:
        server_id = interaction.guild_id
        user_name = interaction.user.name
        with open('data.json', 'r') as data:
            admins = json.loads(data.read())[server_id]['admins']
        if user_name in admins:
            return 'User is already admin'
        else:
            admins.add(user_name)
            return True
    except Exception:
        return False