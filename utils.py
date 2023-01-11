import discord

def get_command(message):
    prefix = "+g"
    if not message.startswith(prefix):
        return None
    # Split the message into a list containing the command and its arguments
    cmd_and_args = message[len(prefix):].split()
    # Return the command (first element in the list)
    return cmd_and_args[0] if cmd_and_args else None
    
def parse_message(message):
    # Split the message into a list by the '-' character
    parts = message.split('-')

    # Get the name by removing the leading and trailing whitespace from the first element in the list
    name = parts[0].strip().split("+g jugador ")[1]

    # Get the description by removing the leading and trailing whitespace from the second element in the list
    description = parts[1].strip()

    # Get the image by removing the leading and trailing whitespace from the third element in the list
    image = parts[2].strip()

    # Return the name, description, and image as an object
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
    # Split the message into a list by the '-' character
    parts = message.split('-')

    # Get the name by removing the leading and trailing whitespace from the first element in the list
    time = parts[0].strip().split("+g partido ")[1]

    # Get the description by removing the leading and trailing whitespace from the second element in the list
    num_players = parts[1].strip()
    print(num_players)

    # Get the image by removing the leading and trailing whitespace from the third element in the list
    day = parts[2].strip()

    # Return the name, description, and image as an object
    return {
        'time': time,
        'num_players': num_players,
        'day': day
    }
