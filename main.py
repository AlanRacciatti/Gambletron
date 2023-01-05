import discord


class MyClient(discord.Client):
    async def on_ready(self):
        print(f'Logged on as {self.user}!')

    async def on_message(self, message):
        if not message.author.bot:
            if message.content.lower() == "esto anda?":
                await message.reply(f"Si {message.author.name}")

intents = discord.Intents.default()
intents.message_content = True

client = MyClient(intents=intents)
client.run('MTA2MDY2MDg1OTA1NzIyNTc5OA.GttDBF.QsCrywXHfNzIyaULpdjnVhwpZVAGUI3N-qc4os')
