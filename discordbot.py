import discord
from discord.ext import commands
import requests

TOKEN = "NzQyMDA2NDY0NjI5MDQ3MzQ5.Xy_1Xg.ME9XuYRNUr8hlAtIVSJCyxtr0cA"
BOT_PREFIX = ("?")

MACAD = "10:7B:44:47:9D:DF"
IPAD = "192.168.11.3"

client = discord.Client()


@client.event
async def on_voice_state_update(member, before, after):
    if after.channel != None and len(after.channel.members) == 1:
        notification_message = f'{member.display_name}がdiscordでボイスチャットを開始しました。'
        line_notify_token = 'zEgycWHrMN5gKgyflG07kKV98VqFxW5qH85FDllikz8'
        line_notify_api = 'https://notify-api.line.me/api/notify'
        headers = {'Authorization': f'Bearer {line_notify_token}'}
        data = {'message': notification_message}
        requests.post(line_notify_api, headers = headers, data = data)


client.run(TOKEN)
