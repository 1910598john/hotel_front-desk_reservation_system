import mysql.connector

mydb = mysql.connector.connect(
  host="localhost",
  user="root",
  password="",
  database='system_user'
)

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE log (islogged VARCHAR(10))")
mycursor.execute("CREATE TABLE rooms (id INT AUTO_INCREMENT PRIMARY KEY, room_id VARCHAR(3), type VARCHAR(20), capacity VARCHAR(20), check_in_date VARCHAR(20), check_out_date VARCHAR(20), availability VARCHAR(20))")
mycursor.execute("CREATE TABLE user (id INT AUTO_INCREMENT PRIMARY KEY, name VARCHAR(20), username VARCHAR(20), password VARCHAR(20), isadmin VARCHAR(10))")