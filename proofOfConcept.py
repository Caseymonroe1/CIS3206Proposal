from nba_api.stats.endpoints import playercareerstats
import os
import openai
import discord
from dotenv import load_dotenv
import random
#from dotenv import load_dotenv
load_dotenv()

TOKEN= "MTA3NTA3MDQ4NTQzNzYyODQ5Ng.GzGVbh.wPpEd-TmOJf5JeAf9tc-ZAmfqPZQpgypcZCj24"
api_key='NGvsPZuxbgk2wJSqpCZHKPTJj'
intents=discord.Intents.default()
intents.message_content=True
client=discord.Client(intents=intents)

@client.event
async def on_ready():
    print("Logged in as a bot {0.user}".format(client))

@client.event
async def on_message(message):
    username = str(message.author).split("#")[0]
    channel = str(message.channel.name)
    user_message = str(message.content)
  
    print(f'Message {user_message} by {username} on {channel}')
  
    if message.author == client.user:
        
        return
  
    if channel == "random":
        print(user_message)
       
        if user_message.lower() == "stats":
            #when user types in hello into discord, bot is able to respond by sending something from the nba api
            #meaning they will work together 
            career = playercareerstats.PlayerCareerStats(player_id='203999') 
            print(career.get_available_data())
            await message.channel.send(career.get_available_data())
            return
        elif user_message.lower() == "chat":
            openai.api_key = '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'
            response = openai.Completion.create(
            model="text-davinci-003",
            prompt="list 5 great NBA players",
            temperature=0.3,
            max_tokens=120,
            top_p=1.0,
            frequency_penalty=0.0,
            presence_penalty=0.0
            )
            await message.channel.send(response.choices[0].text)
        elif user_message.lower() == "tell me a joke":
            jokes = [" Can someone please shed more\
            light on how my lamp got stolen?",
                     "Why is she called llene? She\
                     stands on equal legs.",
                     "What do you call a gazelle in a \
                     lions territory? Denzel."]
            await message.channel.send(random.choice(jokes))


client.run(TOKEN)