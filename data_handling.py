import json
import discord


def create_server(interaction: discord.Interaction):
    try:
        server_id = str(interaction.guild_id)
        new_server_content = {
                "admins": [],
                "polls": {},
                "reference": {
                    "genshin": "gayshitInfect"
                },
            }
        servers = getData()
        servers[server_id] = new_server_content
        saveData(servers)
        return True
    except Exception as e:
        print(e)
        return False

def person_rights(interaction: discord.Interaction):
    try:
        user_is_serveradmin = interaction.user.guild_permissions.administrator
        user_is_botadmin = False
        server_id = str(interaction.guild_id)
        user_name = interaction.user.name
        servers = getData()
        if server_id in servers:
            admins = servers[server_id]['admins']
            user_is_botadmin = user_name in admins
        return [user_is_serveradmin, user_is_botadmin]
    except Exception as e:
        print(e)
        return False

def user_is_admin(interaction: discord.Interaction):
    try:
        server_id = str(interaction.guild_id)
        user_name = interaction.user.name
        user_is_serveradmin = interaction.user.guild_permissions.administrator
        with open('data.json', 'r') as servers:
            server = json.loads(servers.read())
            if server_id in server:
                admins = server[server_id]['admins']
            else:
                create_server(interaction)
                admins = []
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
        server_id = str(interaction.guild_id)
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
    
def addPollToData(interaction: discord.Interaction, name: str):
    defaultPoll = {"votes": {
            },
            "gameList": [       
            ],
            "phase": "voting"}
    user_name = str(interaction.user.name)
    defaultPoll["madeBy"] = user_name
    server_id = str(interaction.guild_id)
    server = getData()
    if server_id in server and name in server[server_id]['polls']:
        return False
    else:
        if server_id in server:
            server[server_id]['polls'][name] = defaultPoll
            saveData(server)
            return True
        else:
            create_server(interaction)
            server = getData()
            server[server_id]['polls'][name] = defaultPoll
            saveData(server)
            return True
            
def getData():
    with open('data.json', 'r') as data:
        admins = json.loads(data.read())
        return admins
    
def saveData(dataToSave):
    with open("data.json", mode="w") as data:
        data.write(json.dumps(dataToSave, indent=4))