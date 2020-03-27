import discord
from auth_data import DC_TOKEN
import datetime
TOKEN = DC_TOKEN

client = discord.Client()


@client.event
async def on_ready():
    print(f'{client.user} has connected to Discord!')


@client.event
async def on_message(message):
    flag = False
    if message.author == client.user:
        return
    if 'help' in message.content.lower():
        await message.channel.send(f"Send me 'set_timer in ! hours ! minutes' to set timer\nI will remind you :)")
    if "set_timer" in message.content.lower():
        hours = int(message.content.lower().split()[2])
        minutes = int(message.content.lower().split()[4])
        await message.channel.send(f"The timer should start in {hours} hours and {minutes} minutes. ")
        date = datetime.datetime.now()
        delta = datetime.timedelta(hours=hours, minutes=minutes)
        flag = True

    if flag:
        while True:
            if datetime.datetime.now() > date + delta:
                await message.channel.send(f'🕒 Time X has come')
                flag = False
                break


client.run(TOKEN)