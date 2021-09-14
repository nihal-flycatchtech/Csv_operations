import csv
import MySQLdb

mydb = MySQLdb.connect(host="127.0.0.1", port=3307, user="root", password="root", database="csv")
with open('myFile0.csv', 'r') as csv_file:
    csv_file = csv.reader(csv_file, delimiter=',')
    next(csv_file)
    all_value = []
    for row in csv_file:
        value = (row[0], row[1], row[2], row[3], row[4])
        all_value.append(value)

query = "insert into csv_table(id, firstname, lastname, email, profession) values (%s, %s, %s, %s, %s)"

mycurser = mydb.cursor()
mycurser.executemany(query, all_value)
mydb.commit()
