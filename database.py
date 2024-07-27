import sqlite3

sqliteConnection = sqlite3.connect('data/db.db')

def query_db(query):
    cursor = sqliteConnection.cursor()
    cursor.execute(query)
    result = cursor.fetchall() 
    cursor.close()
    return result

def execute_db(query): #insert, execute data into database
    cusor = sqliteConnection.cursor()
    cusor.execute(query)
    sqliteConnection.commit()
    cusor.close()

def getMovieByID(id):
    query = f"SELECT * FROM movie WHERE id = {id}"
    return query_db(query)[0]

# def search_movies(search_term):
#     search_term = f"%{search_term}%"
#     query = "SELECT * FROM movie WHERE name LIKE ? OR genre LIKE ?"
#     return query_db(query, (search_term, search_term))

def add_movie(name, release_date, genre, img):
    query = f"INSERT INTO movie (name, release_date, genre, img) VALUES ('{name}', '{release_date}', '{genre}', '{img}')"
    execute_db(query)

def update_movie(id, name, release_date, genre, img):
    query = f"UPDATE movie SET name = {name}, release_date = {release_date}, genre = {genre}, img = {img} WHERE id = {id}"
    execute_db(query)

def remove_movie(id):
    query = f"DELETE FROM movie WHERE id = {id}"
    execute_db(query)

def search_movies(search_term):
    query = f"SELECT * FROM movie WHERE title LIKE {search_term} OR genre LIKE {search_term}"
    return query_db(query)

def get_user_by_id(id):
    query = f"SELECT * FROM USER WHERE id = {id}"
    result = query_db(query)
    return result[0]

def update_user(id, email, username, phone, address, nationality, avatar):
    query = f"UPDATE USER SET email = '{email}', username = '{username}', phone = '{phone}', address = '{address}', nationality = '{nationality}', avatar = '{avatar}' WHERE id = {id}"
    execute_db(query)