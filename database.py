import sqlite3

def create_table():
    conn=sqlite3.connect('Client.db')
    cursor=conn.cursor()

    cursor.execute('''
                   CREATE TABLE IF NOT EXISTS Clients(
                   id TEXT PRIMARY KEY,
                   name TEXT
                   booking date TEXT,
                   location TEXT,
                   transport TEXT,
                   hotels TEXT)''')
    conn.commit()
    conn.close()

def fetch_clients():
    conn=sqlite3.connect('Clients.db')
    cursor=conn.cursor()
    cursor.execute('SELECT* FROM Employees')
    clients= cursor.fetchall()
    conn.close()
    return clients

def insert_client(id,name, booking_date, location, transport, hotel):
    conn=sqlite3.connect('Client.db')
    cursor=conn.cursor()
    cursor.execute('INSERT INTO Client(name, booking date, location, transport, hotel) VALUES(?,?,?,?,?,?)',
                   (id,name, booking_date, location, transport, hotel))
    conn.commit()
    conn.close

def delete_employee(id):
    conn=sqlite3.connect('Client.db')
    cursor=conn.cursor()
    cursor.execute('DELETE FROM Client WHERE id=?', (id,))
    conn.commit()
    conn.close()

def update_client(new_id,new_name, new_booking_date, new_location, new_transport, new_hotel):
    conn= sqlite3.connect('Client.db')    
    cursor=conn.cursor()
    cursor.execute("UPDATE CLIENT SET name=?, booking_date=?, location=?,transport=?, hotel=? WHERE id=?",
                   (new_id,new_name, new_booking_date, new_location, new_transport, new_hotel))
    conn.commit()
    conn.close()

def id_exists(id):
    conn=sqlite3.conect('Client.db')
    cursor=conn.cursor()
    cursor.executte('SELECT COUNT(*) FROM Client WHERE id=?', (id,))
    result=cursor.fetchone()
    conn.close()
    return result[0]>0

create_table()

    




    
