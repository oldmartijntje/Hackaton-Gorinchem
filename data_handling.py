import json
import discord


class DataHandling:
    def create_server(self, interaction: discord.Interaction):
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

    def user_is_admin(self, interaction: discord.Interaction):
        user = interaction.user.name
        user_is_serveradmin = interaction.user.guild_permissions.administrator
        server_id = interaction.guild_id
        with open('servers.json', 'r') as servers:
            admins = json.loads(servers.read())[server_id]['admins']
        user_is_botadmin = user in admins
        if user_is_serveradmin:
            return True
        elif user_is_botadmin:
            return True
        else:
            return False



