import mysql.connector as m


mydb = m.connect(
    host = 'localhost',
    user ='root',
    passwd = '',
    port = '3306',
    database = 'testdb'
)


my_cursor = mydb.cursor()
# my_cursor.execute("CREATE DATABASE testdb")
my_cursor.execute("SHOW DATABASES")
for db in my_cursor:
    print(db[0])