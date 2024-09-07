import discord
import re

intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)
DISCORD_TOKEN = 'MTI4MTU1ODQ2MTczMzI3Nzc1OA.Gay4Jt.ColCDAu5yApyqkbUTDYfrMrKyxmRTW8GjJ16ds'

@client.event
async def on_ready():
    print(f'Logged in as {client.user}')
    for guild in client.guilds:
        print(f"เซิร์ฟเวอร์: {guild.name}")
        members = '\n'.join([member.name for member in guild.members])
        print(f"รายชื่อสมาชิกทั้งหมดในเซิร์ฟเวอร์:\n{members}")

@client.event
async def on_message(message):
    if message.author == client.user:
        return  # ข้ามข้อความที่บอทส่งเอง

    # ตรวจสอบว่าข้อความถูกส่งใน Direct Message (DM)
    if isinstance(message.channel, discord.DMChannel):
        print(f"DM จาก {message.author}: {message.content}")
        for guild in client.guilds:
            channel = discord.utils.get(guild.text_channels, name="bot-communication")
            
            if channel:
                try:
                    await channel.send(f"21358743.{message.content}.{message.author.name}.653745106654")
                    await message.channel.send("ข้อความของคุณถูกส่งไปยัง bot-communication แล้ว!")
                except discord.Forbidden:
                    await message.channel.send("ไม่สามารถส่งข้อความไปที่ bot-communication ได้")
            else:
                await message.channel.send("ไม่พบช่อง bot-communication ในเซิร์ฟเวอร์")
    
    # ตรวจสอบว่าเป็นข้อความจาก Text Channel (ไม่ใช่ DM)
    elif isinstance(message.channel, discord.TextChannel):
        if message.channel.name != "bot-communication":
            return

        print(message.content)
        print(type(message.content))    

        match = re.match(r'(\d+)\.(.*?)\.(\d+)', message.content)
    
        print(match)

        if match:
            number_front = match.group(1)
            user_name = match.group(2)
            number_back = match.group(3)
        
            print(number_front, user_name, number_back)
            
            if number_front == "546187845659854321" and number_back == "168461168684":
                guild = message.guild
                member = discord.utils.get(guild.members, name=user_name)
            
                if member:
                    try:
                        await member.send("คุณอยากคุยกับใคร\nI Mie ai กด 1")
                        await message.channel.send(f"ส่ง DM ถึง {member.name} เรียบร้อยแล้ว")
                    except discord.Forbidden:
                        await message.channel.send(f"ไม่สามารถส่ง DM ให้ {member.name} ได้")
                else:
                    await message.channel.send(f"ไม่พบผู้ใช้ชื่อ {user_name} ในเซิร์ฟเวอร์นี้")
            else:
                await message.channel.send("ตัวเลขด้านหน้าและด้านหลังไม่ตรงกัน")
        else:
            await message.channel.send("รูปแบบข้อความไม่ถูกต้อง")

client.run(DISCORD_TOKEN)
