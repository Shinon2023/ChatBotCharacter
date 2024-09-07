import discord

intents = discord.Intents.default()
intents.message_content = True
client = discord.Client(intents=intents)
DISCORD_TOKEN = 'MTI3OTgxODgyMDg0Mzg2NDEwNA.Gd69Ji.K1UjBgOngh9zZf3_qukoIZ8fiD7ePZfel015-0'

@client.event
async def on_ready():
    print(f'ล็อกอินเป็น {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    if message.channel.name == "guide":
        guild = message.guild
        channel = discord.utils.get(guild.text_channels, name="bot-communication")
        
        if channel:
            try:
                await channel.send(f"546187845659854321.{message.author.name}.168461168684")
            except discord.Forbidden:
                await message.channel.send(f"ไม่สามารถส่งข้อความไปที่ช่อง {channel.name} ได้")
        else:
            await message.channel.send("ไม่พบช่อง bot-communication")

client.run(DISCORD_TOKEN)
