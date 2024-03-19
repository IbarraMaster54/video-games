#import database engine
import sqlite3

#Create database connection (DB_NAME)
dbName = 'mygame'
con = sqlite3.connect(dbName)

#Enable to execute CRUD commands/querys
cur = con.cursor()

#Create users table
player_table = ''' 
    CREATE TABLE IF NOT EXISTS players(
        id INTEGER PRIMARY KEY, 
        fullname TEXT NOT NULL,
        nickname TEXT NOT NULL,
        email TEXT NOT NULL,
        password TEXT NOT NULL,
        status BOOLEAN DEFAULT true,
        created_at TIMESTAMP DEFAULT (datetime('now', 'localtime')),
        updated_at TIMESTAMP NULL,
        deleted_at TIMESTAMP NULL
    )
'''

#Execute query
cur.execute(player_table)

#send changes 
con.commit()