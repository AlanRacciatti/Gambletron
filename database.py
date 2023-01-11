import mysql.connector

def create(name, description, image):
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='gambletron')

    # Create a cursor
    cursor = cnx.cursor()

    # Execute the INSERT statement
    query = "INSERT INTO players (name, description, image) VALUES (%s, %s, %s)"
    values = (name, description, image)
    cursor.execute(query, values)

    # Commit the changes to the database
    cnx.commit()

    # Close the connection
    cnx.close()

def create_games(time, num_players, day):
    print("create_games")
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='gambletron')

    # Create a cursor
    cursor = cnx.cursor()

    # Execute the INSERT statement
    query = "INSERT INTO games (time, num_players, day) VALUES (%s, %s, %s)"
    values = (time, num_players, day)
    cursor.execute(query, values)

    # Commit the changes to the database
    cnx.commit()

    # Close the connection
    cnx.close()

def read():
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='gambletron')

    # Create a cursor
    cursor = cnx.cursor()

    # Execute the SELECT statement
    query = "SELECT * FROM players"
    cursor.execute(query)

    # Fetch the results
    result = cursor.fetchall()

    # Close the connection
    cnx.close()

    return result

def readById(id):
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='gambletron')

    # Create a cursor
    cursor = cnx.cursor()

    # Execute the SELECT statement
    query = "SELECT * FROM players WHERE id = %s"
    values = (id,)
    cursor.execute(query, values)

    # Fetch the results
    result = cursor.fetchone()

    # Close the connection
    cnx.close()

    return result

def update(id, name, description, image):
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='gambletron')

    # Create a cursor
    cursor = cnx.cursor()

    # Execute the UPDATE statement
    query = "UPDATE players SET name = %s, description = %s, image = %s WHERE id = %s"
    values = (name, description, image, id)
    cursor.execute(query, values)

    # Commit the changes to the database
    cnx.commit()

    # Close the connection
    cnx.close()

# def add_players(id):
#     from functions import player_id

#     cnx = mysql.connector.connect(user='root', password='', host='localhost', database='gambletron')

#     # Create a cursor
#     cursor = cnx.cursor()

#     # Execute the UPDATE statement
#     query = f"UPDATE games SET players = {player_id(id)} WHERE id = id"
#     values = (player)
#     cursor.execute(query, values)

#     # Commit the changes to the database
#     cnx.commit()

#     # Close the connection
#     cnx.close()


def delete(id):
    # Connect to the database
    cnx = mysql.connector.connect(user='root', password='', host='localhost', database='gambletron')

    # Create a cursor
    cursor = cnx.cursor()

    # Execute the DELETE statement
    query = "DELETE FROM players WHERE id = %s"
    values = (id,)
    cursor.execute(query, values)

    # Commit the changes to the database
    cnx.commit()

    # Close the connection
    cnx.close()
