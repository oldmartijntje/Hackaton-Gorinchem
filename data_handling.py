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

def person_rights(interaction: discord.Interaction, thing_to_say):
    try:
        if user_is_admin(interaction):
            if thing_to_say.startswith('<@') and thing_to_say.endswith('>'):
                user_id = thing_to_say[2:][:-1]
            else:
                return False, 'Please mention the user who you want to give admin rights.'
            user_is_serveradmin = interaction.user.guild_permissions.administrator
            user_is_botadmin = False
            server_id = str(interaction.guild_id)
            servers = getData()
            if server_id in servers:
                admins = servers[server_id]['admins']
                user_is_botadmin = user_id in admins
            return True, {"server_admin": user_is_serveradmin, "bot_admin": user_is_botadmin}
        else:
            return False, 'You do not have permission to view this content.'
    except Exception as e:
        print(e)
        return False, 'Something went wrong.'

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
        user_name = interaction.user.id
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


def add_botadmin(interaction: discord.Interaction, thing_to_say):
    try:
        if thing_to_say.startswith('<@') and thing_to_say.endswith('>'):
            user_id = thing_to_say[2:][:-1]
        else:
            return 'Please mention the user who you want to give admin rights.'
        server_id = str(interaction.guild_id)
        data = getData()
        if server_id in data:
            admins = data[server_id]['admins']
            if user_id in admins:
                return 'User already had admin rights.'
            else:
                admins.append(user_id)
                saveData(data)
                return 'User now has admin rights.'
        else:
            create_server(interaction)
            return 'User now has admin rights.'
    except Exception as e:
        print(e)
        return 'Something went wrong.'

def remove_botadmin(interaction: discord.Interaction, thing_to_say):
    try:
        if thing_to_say.startswith('<@') and thing_to_say.endswith('>'):
            user_id = thing_to_say[2:][:-1]
        else:
            return 'Please mention the user whose admin rights you want to revoke.'
        server_id = str(interaction.guild_id)
        data = getData()
        if server_id in data:
            admins = data[server_id]['admins']
            if user_id in admins:
                admins.remove(user_id)
                saveData(data)
                return 'User no longer has admin rights.'
            else:
                return 'User had no admin rights.'
        else:
            create_server(interaction)
            return 'User no longer has admin rights.'
    except Exception as e:
        print(e)
        return 'Something went wrong.'
    
def addPollToData(interaction: discord.Interaction, name: str):
    defaultPoll = {"votes": {
            },
            "gameList": [       
            ],
            "phase": "adding"}
    user_name = str(interaction.user.id)
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

# jurrians code start
def get_admin_list(interaction: discord.Interaction):
    try:
        server_id = str(interaction.guild_id)
        data = getData()
        if server_id in data:
            admins = ''
            admin_list = data[server_id]['admins']
            if len(admin_list) == 0:
                return 'No admins.'
            for admin in admin_list:
                admins += f'\n- <@{admin}>'
            return admins
        else:
            return 'Admins couldn\'t be found.'
    except:
        return 'Something went wrong.'



# jurrians code einde