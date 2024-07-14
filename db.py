import sqlite3

sqliteConnection = sqlite3.connect('data/user.db')
def execute_db(query): #insert, execute data in table
    cusor = sqliteConnection.cursor()
    cusor.execute(query)
    sqliteConnection.commit()
    cusor.close()

def query_db(query):
    cursor = sqliteConnection.cursor()
    cursor.execute(query)
    result = cursor.fetchall() #check if the result was in db(in list)
    cursor.close()
    return result

def create_user(email, password, name):
    query = f"INSERT INTO USER (email, password, name) VALUES ('{email}', '{password}', '{name}')"
    execute_db(query)
    
def get_user_by_email(email):
    query = f"SELECT * FROM USER WHERE email = '{email}'"
    result = query_db(query)
    return result

def get_user_by_id(id):
    query = f"SELECT * FROM USER WHERE id = {id}"
    result = query_db(query)
    return result

def get_user_by_email_password(email, password):
    query = f"SELECT * FROM USER WHERE email ='{email}' and password='{password}'"
    result = query_db(query)
    return result

def update_user(id, email, username, phone, address, nationality):
    query = f"UPDATE USER SET email = '{email}', username = '{username}', phone = '{phone}', address = '{address}', nationality = '{nationality}' WHERE id = {id}"
    execute_db(query)

    