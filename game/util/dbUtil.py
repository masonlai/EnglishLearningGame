import sqlite3


def connect():
    con = sqlite3.connect('db')
    # cur = con.cursor()
    return con


def disconnect(con):
    con.commit()
    con.close()


def updateWGG(name, score, time):
    con = connect()
    cur = con.cursor()
    insertSQL = 'insert into WGG VALUES (?, ?, ?);'
    SQLdata = (name, score, str(time))
    cur.execute(insertSQL, SQLdata)
    disconnect(con)

def updateROG(name, score, time):
    con = connect()
    cur = con.cursor()
    insertSQL = 'insert into ROG VALUES (?, ?, ?);'
    SQLdata = (name, score, str(time))
    cur.execute(insertSQL, SQLdata)
    disconnect(con)


def updateVBG(name, score, time):
    con = connect()
    cur = con.cursor()
    insertSQL = 'insert into VBG VALUES (?, ?, ?);'
    SQLdata = (name, score, str(time))
    cur.execute(insertSQL, SQLdata)
    disconnect(con)

def top10WGG():
    con = connect()
    cur = con.cursor()

    cur.execute("SELECT * FROM WGG order by score desc LIMIT 10")

    rows = cur.fetchall()

    return rows

def top10ROG():
    con = connect()
    cur = con.cursor()

    cur.execute("SELECT * FROM ROG order by score desc LIMIT 10")

    rows = cur.fetchall()

    return rows

def top10VBG():
    con = connect()
    cur = con.cursor()

    cur.execute("SELECT * FROM VBG order by score desc LIMIT 10")

    rows = cur.fetchall()

    return rows