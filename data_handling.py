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

def get_poll_list(interaction: discord.Interaction):
    try:
        data = getData()
        server_id = str(interaction.guild_id)
        if server_id in data:
            polls = data[str(interaction.guild_id)]["polls"]
            prettified_poll_list = ''
            for poll in polls:
                prettified_poll_list += '\n- ' + poll
            if len(polls) == 0:
                return 'There are currently no polls available.'
            else:
                return prettified_poll_list
        else:
            create_server(interaction)
            return 'There are currently no polls available.'
        
    except Exception as e:
        print(e)
        return {}

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
        data = getData()
        if server_id in data:
            admins = data[server_id]['admins']
            if user_name in admins:
                return 'User is already admin'
            else:
                admins.append(user_name)
                saveData(data)
                return True
        else:
            create_server(interaction)
            return True
    except Exception as e:
        print(e)
        return False

def remove_botadmin(interaction: discord.Interaction):
    try:
        server_id = str(interaction.guild_id)
        user_name = interaction.user.name
        data = getData()
        if server_id in data:
            admins = data[server_id]['admins']
            if user_name in admins:
                admins.remove(user_name)
                saveData(data)
                return True
            else:
                return 'User was not an admin'
        else:
            create_server(interaction)
            return True
    except Exception as e:
        print(e)
        return False
    
def addPollToData(interaction: discord.Interaction, name: str):
    defaultPoll = {"votes": {
            },
            "gameList": [       
            ],
            "phase": "adding"}
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
            
# emiels code start hier
# emiels code endigt hier


def getData():
    checkIfExist()
    with open('data.json', 'r') as data:
        admins = json.loads(data.read())
        return admins
    
def saveData(dataToSave):
    with open("data.json", mode="w") as data:
        data.write(json.dumps(dataToSave, indent=4))

def checkIfExist():
    import os
    if not os.path.isfile('data.json'):
        with open("data.json", mode="w") as data:
            data.write(json.dumps({}, indent=4))