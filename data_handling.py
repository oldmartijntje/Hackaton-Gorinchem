import json
import discord


class DataHandling:
    def create_server(self, server_id, interaction: discord.Interaction):
        try:
            with open('data.json', 'r') as server_data:
                new_server_data = json.loads(server_data.read())['testServerId']
            with open('data.json', 'w') as servers:
                json.loads(servers.read())[server_id] = new_server_data
            return True
        except Exception as e:
            print(e)
            return False



