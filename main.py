import discord
import mysql.connector
from database import *
from utils import *
import os
from dotenv import load_dotenv
import time
load_dotenv()

class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if not message.author.bot and message.content.startswith("+g"):
            command = get_command(message.content)
            if command == "jugador":
                data= parse_message(message.content)
                create(data["name"], data["description"], data["image"])
                await message.reply(f"se creo el jugador con el nombre {data['name']}")
                print(readById(1))
            elif command == "partido":
                datas= game(message.content)
                create_games(datas["time"], datas["num_players"], datas["day"])
                await message.reply(f"quienes iran al partido? \n{players_str(read())}")
                pedo = []
                for f in range (int(datas["num_players"])):
                    time.sleep(5)
                    if command == str(f):
                        time.sleep(5)
                        pedo.append(f)
                    print(pedo)
                await message.reply(f"se creo el partido el {datas['day']} a las {datas['time']}")
            elif command == "jugadores":
                lista = players_str(read())
                await message.reply(lista)
            elif command == "help":
                await message.reply(player_id(3))

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("TOKEN"))
