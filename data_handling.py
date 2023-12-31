import json
import discord

# martijns code start hier
def doesPollExist(interaction: discord.Interaction, poll):
    data = getData()
    server_id = str(interaction.guild_id)
    if server_id in data:
        if poll in data[server_id]["polls"]:
            return True
        else:
            return False
    else:
        return False
    
def calculateWinner(interaction: discord.Interaction, poll_name):
    import operator
    try:
        server_id = str(interaction.guild_id)
        data = getData()
        winnerDict = {}
        top3Dict = {"number1":"",
                   "number1amount":0,
                   "number2":"",
                   "number2amount":0,
                   "number3":"",
                   "number3amount":0}
        for voter in data[server_id]["polls"][poll_name]["votes"]:
            for x in range(3):
                if data[server_id]["polls"][poll_name]["votes"][voter][f"{x+1}points"] == "":
                    pass
                elif data[server_id]["polls"][poll_name]["votes"][voter][f"{x+1}points"] not in data[server_id]["polls"][poll_name]["gameList"]:
                    pass
                else:
                    if data[server_id]["polls"][poll_name]["votes"][voter][f"{x+1}points"] not in winnerDict:
                        winnerDict[data[server_id]["polls"][poll_name]["votes"][voter][f"{x+1}points"]] = x+1
                    else:
                        winnerDict[data[server_id]["polls"][poll_name]["votes"][voter][f"{x+1}points"]] += x+1
                    if winnerDict[data[server_id]["polls"][poll_name]["votes"][voter][f"{x+1}points"]] > top3Dict["number1amount"]:
                        top3Dict["number1"] = data[server_id]["polls"][poll_name]["votes"][voter][f"{x+1}points"]
                        top3Dict["number1amount"] = winnerDict[data[server_id]["polls"][poll_name]["votes"][voter][f"{x+1}points"]]
                    elif winnerDict[data[server_id]["polls"][poll_name]["votes"][voter][f"{x+1}points"]] > top3Dict["number2amount"]:
                        top3Dict["number2"] = data[server_id]["polls"][poll_name]["votes"][voter][f"{x+1}points"]
                        top3Dict["number2amount"] = winnerDict[data[server_id]["polls"][poll_name]["votes"][voter][f"{x+1}points"]]
                    elif winnerDict[data[server_id]["polls"][poll_name]["votes"][voter][f"{x+1}points"]] > top3Dict["number3amount"]:
                        top3Dict["number3"] = data[server_id]["polls"][poll_name]["votes"][voter][f"{x+1}points"]
                        top3Dict["number3amount"] = winnerDict[data[server_id]["polls"][poll_name]["votes"][voter][f"{x+1}points"]]
        winnerDict = sorted(winnerDict.items(), key=operator.itemgetter(1))
        return top3Dict

    except Exception as e:
        print(e)


def winnerDictFormatted(interaction: discord.Interaction, top3Dict):
    text = ""
    for x in range(3):
        if top3Dict[f"number{x+1}"] !="":
            text += f"\n- {x+1}.`{top3Dict[f'number{x+1}']}` with {top3Dict[f'number{x+1}amount']} votes!"
    if text != "":
        return "Here are the results: " + text
    else:
        return False
# martijns code eindigt hier

def create_server(interaction: discord.Interaction):
    try:
        serverName = interaction.guild.name
        server_id = str(interaction.guild_id)
        new_server_content = {
                "admins": [],
                "polls": {},
                "reference": {
                    "genshin": "gayshitInfect"
                },
                "serverName": serverName,
                "directMessages": True
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
                prettified_poll_list += '\n- `' + poll+'`'
                if data[server_id]["polls"][poll]["phase"] == "adding":
                    prettified_poll_list += f"    📝items addable📝"
                elif data[server_id]["polls"][poll]["phase"] == "voting":
                    prettified_poll_list += f"    🗳able to vote🗳"
                else:
                    prettified_poll_list += f"    🔒vote is closed🔒"
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

def delete_poll(interaction: discord.Interaction, thing_to_say):
    try:
        if user_is_admin(interaction):
            poll_name = thing_to_say
            data = getData()
            server_id = str(interaction.guild_id)
            if server_id in data:
                polls = data[server_id]['polls']
                if thing_to_say in polls:
                    del polls[poll_name]
                    saveData(data)
                else:
                    return 'Poll does not exist.'
            return f'Successfully deleted poll {poll_name}!'
        else:
            return 'You do not have permission to delete this poll.'
    except Exception as e:
        print(e)
        return 'Something went wrong.'
# jurrians code einde