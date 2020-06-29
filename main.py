import mysql.connector

db = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database="mydatabase"
)
cur = db.cursor()

sql = "SELECT * FROM customers WHERE address ='Park Lane 38'"

cur.execute(sql)

myresult = cur.fetchall()

for x in myresult:
  print(x)