import sqlite3
con = sqlite3.connect('game.db')


cur = con.cursor()

# Create table
cur.execute('''CREATE TABLE WGG
               (Name TEXT, score INTEGER, date TEXT)''')

cur.execute('''CREATE TABLE ROG
               (Name TEXT, score INTEGER, date TEXT)''')

cur.execute('''CREATE TABLE VBG
               (Name TEXT, score INTEGER, date TEXT)''')


# Save (commit) the changes
con.commit()

# We can also close the connection if we are done with it.
# Just be sure any changes have been committed or they will be lost.
con.close()