import mysql.connector

con = mysql.connector.connect(
    user = "username",
    password = "password",
    host = "host_address",
    database = "database_name"
)

cursor = con.cursor() 

word = input("Enter a word: ")

query = cursor.execute("SELECT * FROM Dictionary WHERE Expression = '%s' " % word)
results = cursor.fetchall()

if results:
    for result in results:
        print(result[1])
else:
    print("No word found!")