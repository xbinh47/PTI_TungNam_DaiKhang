import sqlite3

sqliteConnection = sqlite3.connect('data/db.db')
def query_db(query):
    cursor = sqliteConnection.cursor()
    cursor.execute(query)
    result = cursor.fetchall() #check if the result was in db(in list)
    cursor.close()
    return result

def getVideoByID(id):
    query = f"SELECT * FROM movie WHERE id = {id}"
    return query_db(query)[0]