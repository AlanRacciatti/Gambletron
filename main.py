import discord
import mysql.connector
from database import *
from utils import *
import os
from dotenv import load_dotenv
import time
import datetime
import asyncio
import random
from discord.ext import commands 
load_dotenv()


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')
    
        client = commands.Bot(command_prefix = "+", help_command=None)

        @client.command()
        async def test(ctx, role: discord.Role, user: discord.Member):
            await user.add_roles(role)

    async def on_message(self, message):
        if not message.author.bot and message.content.startswith("+g"):
            command = get_command(message.content)
            print("sexo2")
            # crear perfil del jugador con descripcion y su imagen

            if command == "jugador":
                data= parse_message(message.content)
                create(data["name"], data["description"], data["image"])
                await message.reply(f"se creo el jugador con el nombre {data['name']}")
                print(readById(1))

            # crear partido que se vaya a jugar, incluyendo a que hora, cantidad de jugadores, y el dia

            elif command == "partido":
                datas= game(message.content)
                create_games(datas["time"], datas["num_players"], datas["day"])
                await message.reply(f"quienes iran al partido? \n{players_str(read())}")
                await message.reply(f"se creo el partido el {datas['day']} a las {datas['time']}")

            #  ver lista de todos los jugadores

            elif command == "jugadores":
                lista = players_str(read())
                await message.reply(lista)
            
            # borrar todos los mensajes del chat

            elif command == "clean":
                pass

            # colocar audio en chat de voz

            elif command == "audio":
                if message.author.voice:
                    voice_channel = message.author.voice.channel
                    vc = await voice_channel.connect()
                    vc.play(discord.FFmpegPCMAudio(audios()), after=lambda e: print('done', e))
                    vc.source = discord.PCMVolumeTransformer(vc.source)
                    vc.source.volume = 1
                    await asyncio.sleep(7)
                    await vc.disconnect()
                else:
                    await message.channel.send("primero debes entrar a un canal de voz!")    

            elif command == "ja":
                await message.reply("+p $add-money-role @PASAJEROS  5000000")

            else:
                await message.channel.send("ese comando no existe.")
            

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run(os.getenv("TOKEN"))
