import os
import random
import discord
from dotenv import load_dotenv

load_dotenv()
TOKEN = 'ODAxODY2ODc2OTIwNTI4OTE2.YAm6uQ.bmRlWcT6q1mQbXLvkcz1j8xsvHU'

client = discord.Client()

OnOff = ['On','Off']
Meetings = ['0','1','2','3','4','5','6','7','8','9']
Emergency = ['0,5','10','15','20','25','30','35','40','45','50','55','60']
Discussion = ['0','15','30','45','60','75','90','105','120']
Vote = ['0','15','30','45','60','75','90','105','120','135','150','165','180','195','210','225','240','255','270','285','300']
Speed = ['0.5','0.75','1.0','1.25','1.5','.75','2','2.25','2.5','2.75','3']
Vision = ['0.25','0.5','0.75','1','1.25','1.5','1.75','2','2.25','2.5','2.75','3','3.25','3.5','3.75','4','4.25','4.5','4.75','5']
Kill = ['10','12.5','15','17.5','20','22.5','25','27.5','30','32.5','35','37.5','40','42.5','45','47.5','50','52.5','55','57.5','60']
Distance = ['Short','Medium','Long']
TaskBar = ['Always','Meetings','Never']
Common = str(random.randint(0,2))
Long = str(random.randint(0,3))
Short = str(random.randint(0,5))

@client.event
async def on_message(message):
    if message.author == client.user:
        return

    ConfirmEjects = 'Confirm Ejects: ' + random.choice(OnOff)
    EmergencyMeetings = 'Emergency Meetings: ' + random.choice(Meetings)
    Cooldown = 'Emergency Cooldown: ' + random.choice(Emergency)
    DiscussionTime = 'Discussion Time: ' + random.choice(Discussion)
    VotingTime = 'Voting Time: ' + random.choice(Vote)
    PlayerSpeed = 'Player Speed: ' + random.choice(Speed)
    CrewVision = 'Crewmate Vision: ' + random.choice(Vision)
    ImpVision = 'Imposter Vision: ' + random.choice(Vision)
    KillCool = 'Kill Cooldown: ' + random.choice(Kill)
    KillDist = 'Kill Distance: ' + random.choice(Distance)
    VisualTasks = 'Visual Tasks: ' + random.choice(OnOff)
    TBUpdate = 'Taskbar Updates: ' + random.choice(TaskBar)
    CommonTasks = 'Common Tasks: ' + Common
    LongTasks = 'Long Tasks: ' + Long
    ShortTasks = 'Short Tasks: ' + Short

    if message.content == '!Ramongus':
        response = ConfirmEjects,\
                   EmergencyMeetings,\
                   Cooldown,\
                   DiscussionTime,\
                   VotingTime,\
                   PlayerSpeed,\
                   CrewVision,\
                   ImpVision,\
                   KillCool,\
                   KillDist,\
                   VisualTasks,\
                   TBUpdate,\
                   CommonTasks,\
                   LongTasks,\
                   ShortTasks
        await message.channel.send(response)

client.run(TOKEN)

#Code to run: 'python RAmongUs.py', then !Ramongus in discord