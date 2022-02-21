import discord
import json


def main(mess):

    with open("../config.json", "r") as f:
        data = json.load(f)
        print(data)

    token = data["token"]
    print(token)

    client = discord.Client()

    @client.event
    async def on_ready():
        print('Logged in as user {}'.format(client.user.name))
        channel = client.get_channel(796477959766278264)
        await channel.send(mess)

    client.run(token)

