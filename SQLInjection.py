import sqlite3
import os


SQL_QUERY = 'SELECT * FROM test_table WHERE USERNAME = "%s" AND PASSWORD = "%s";'


print("Default SQL Query:", SQL_QUERY)

username = input("\nUsername: ")
password = input("Password: ")

SQL_QUERY = SQL_QUERY % (username, password)

print("\nNew SQL Query:", SQL_QUERY)


INITIALIZE_DB = not os.path.isfile('test_file.db')
db = sqlite3.connect('test_file.db')

if INITIALIZE_DB:
	db.execute("CREATE TABLE test_table (ID INTEGER PRIMARY KEY, USERNAME VARCHAR(255) NOT NULL, PASSWORD VARCHAR(255) NOT NULL);")
	db.execute("INSERT INTO test_table (USERNAME, PASSWORD) VALUES('%s', '%s');" % ("Vbrawl", "Password123"))
	db.commit()

cur = db.execute(SQL_QUERY)
for id, username, password in cur.fetchall():
	print(f"{username} ({id}): {password}")
