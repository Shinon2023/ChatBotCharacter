import discord
import re
from Model.Mie_Ai_Model import MieAIModel

DISCORD_TOKEN = 'MTI4MTU1NjIzMDg0NTg5MDU2Mg.Gj_7_F.mAj2Kbakv62X_zUaX2vlALdbRziflWatWo236I'

# กำหนดค่า intents
intents = discord.Intents.default()
intents.message_content = True
intents.members = True

client = discord.Client(intents=intents)

@client.event
async def on_ready():
    print(f'We have logged in as {client.user}')

@client.event
async def on_message(message):
    if message.author == client.user:
        return
    
    if isinstance(message.channel, discord.TextChannel) and message.channel.name == "bot-communication":
        match = re.match(r'(21358743)\.(.*?)\.(.*?)\.(653745106654)', message.content)

        if match:
            number_front = match.group(1)
            text = match.group(2)
            username = match.group(3)
            number_back = match.group(4)
            if text.lower() != "1":
                return  # ข้ามการทำงานต่อไปและออกจากฟังก์ชันทันที
            elif number_back == "653745106654" and number_front == "21358743":
                guild = message.guild
                member = discord.utils.get(guild.members, name=username)
                if member:
                    try:
                        await member.send(f"สวัสดี {member.name} ยินดีที่ได้รู้จักนะ!")
                        await message.channel.send(f"ส่ง DM ถึง {member.name} เรียบร้อยแล้ว")
                    except discord.Forbidden:
                        await message.channel.send(f"ไม่สามารถส่ง DM ให้ {member.name} ได้")
                else:
                    await message.channel.send(f"ไม่พบผู้ใช้ชื่อ {username} ในเซิร์ฟเวอร์นี้")


    elif isinstance(message.channel, discord.DMChannel):
        if message.content.strip():
            try:
                user_input = message.content
                response = MieAIModel().call_ai(user_input)
                await message.channel.send(response)
            except Exception as e:
                await message.channel.send(f"เกิดข้อผิดพลาดในการตอบกลับ: {str(e)}")
        else:
            await message.channel.send("ข้อความที่ส่งมาว่างเปล่า กรุณาลองใหม่อีกครั้ง")

client.run(DISCORD_TOKEN)
