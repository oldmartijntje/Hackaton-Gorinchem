import json
import discord


def create_server(interaction: discord.Interaction):
    try:
        server_id = interaction.guild_id
        with open('data.json', 'r') as server_data:
            new_server_data = json.loads(server_data.read())['testServerId']
        with open('data.json', 'w') as servers:
            json.loads(servers.read())[server_id] = new_server_data
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
            admins = json.loads(servers.read())[server_id]['admins']
        user_is_botadmin = user_name in admins
        if user_is_serveradmin:
            return True
        elif user_is_botadmin:
            return True
        else:
            return False
    except Exception:
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