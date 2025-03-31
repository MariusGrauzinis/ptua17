import sqlite3

conn = sqlite3.connect("people.sqlite")
c = conn.cursor()
with conn:
    c.execute("INSERT INTO friends VALUES ('Dominic', 'Rockwell', 'd.rockwell@company.com')")
    c.execute("INSERT INTO friends VALUES ('Richard', 'Rodman', 'RR@gmail.com')")




with conn:
    c.execute("SELECT * FROM friends WHERE l_name='Rockwell'")
    print(c.fetchall())