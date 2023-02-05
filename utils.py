import discord

def get_command(message):
    prefix = "+g"
    if not message.startswith(prefix):
        return None
    cmd_and_args = message[len(prefix):].split()
    return cmd_and_args[0] if cmd_and_args else None
    
def parse_message(message):
    parts = message.split('-')
    name = parts[0].strip().split("+g jugador ")[1]
    description = parts[1].strip()
    image = parts[2].strip()
    return {
        'name': name,
        'description': description,
        'image': image
    }

def players_str(list):
    response = ""
    for player in list:
        id = player[0]
        name = player[1]
        response += f"{id}. {name}\n"
    return response

def players_tupla(list):
    from database import readById
    players = ""
    for i in range(1, len(list)+1):
        cont = 0
        for a in readById(i):
            if not cont > 1:
                players = players+"- "+str(a)
                cont += 1
        players = players+"\n"
    return players

def player_id(id):
    from database import readById
    player = ""
    cont = 0
    for a in readById(id):
        cont += 1
        if cont == 2:
            player = player + str(a) 
    return player

def list_players_match(id):
    list_id = []
    for i in id:
        if not i == "-":
            list_id.append(i)
    return list_id

def game(message):
    print("games")
    parts = message.split('-')
    time = parts[0].strip().split("+g partido ")[1]
    num_players = parts[1].strip()
    print(num_players)
    day = parts[2].strip()
    return {
        'time': time,
        'num_players': num_players,
        'day': day
    }

def audios():
    import random
    audio_1 = "audios/partido/partido_1.mp3"
    audio_2 = "audios/partido/partido_1.mp3"
    audio_3 = "audios/partido/partido_2.mp3"
    a = random.randint(1,3)
    if a == 1:
        return audio_1
    elif a == 2:
        return audio_2
    else:
        return audio_3

def audio():
    import random
    audio_1 = "audios/random/audio_1.mp3"
    audio_2 = "audios/random/audio_2.mp3"
    audio_3 = "audios/random/audio_3.mp3"
    audio_4 = "audios/random/audio_4.mp3"
    audio_5 = "audios/random/audio_5.mp3"
    audio_6 = "audios/random/audio_6.mp3"
    audio_7 = "audios/random/audio_7.mp3"

    a = random.randint(1,6)
    if a == 1:
        return audio_1
    elif a == 2:
        return audio_2
    elif a == 3:
        return audio_3
    elif a == 4:
        return audio_4
    elif a == 5:
        return audio_5
    elif a == 6:
        return audio_6
    else:
        return audio_7

async def clear(ctx):
    channel = ctx.channel
    await channel.purge()
