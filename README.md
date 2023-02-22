# CIS3296Proposal
Compiled on Windows 11 Pro Version 21H2
Compiled using Python 3.11.0

To run this code, the user must install the python libraries nba_api, discord, dotenv, openai.
This can be done by using pip install for each of these libraries.
The user must create their own tokens for the discord api and the openai api.  The tokens that are listed in the code are just there for example
and have been reset.
To do this, the user can reference this guide on making a discord bot: https://www.geeksforgeeks.org/building-a-discord-bot-in-python/
To get a token for the openai API, the user must create an account and retreive their key from the openai website.

After doing this, the user can clone this repository and run the code with their own discord server.  

![image](https://user-images.githubusercontent.com/82054873/220517509-c8fed004-9793-45b4-9b1f-b1445363c26f.png)
Here is an example of this discord bot working.  As a response to "stats" it will print out sample output from the nba_api library.  
As a response to "chat" it asks the openai API to list out its favorite 5 NBA players.  
