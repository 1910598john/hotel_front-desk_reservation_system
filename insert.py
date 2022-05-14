import mysql.connector
mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='',
    database='system_user'
)

mycursor = mydb.cursor()
room_id = 101
rooms = 60
sql = "INSERT INTO rooms (room_id, type, capacity, check_in_date, check_out_date, availability) VALUES (%s, %s, %s, %s, %s, %s)"
for x in range(rooms):
    if x < 10:
        val = (room_id, "STANDARD", "SINGLE", "5/14/22", "5/15/22", "Available")
    elif x > 10 and x < 20:
        val = (room_id, "STANDARD", "DOUBLE", "5/14/22", "5/15/22", "Available")
    elif x > 20 and x < 30:
        val = (room_id, "ECONOMY", "SINGLE", "5/14/22", "5/15/22", "Available")
    elif x > 30 and x < 40:
        val = (room_id, "ECONOMY", "DOUBLE", "5/14/22", "5/15/22", "Available")
    elif x > 40 and x < 50:
        val = (room_id, "VIP", "SINGLE", "5/14/22", "5/15/22", "Available")
    elif x > 40 and x < 60:
        val = (room_id, "VIP", "DOUBLE", "5/14/22", "5/15/22", "Available")
    room_id += 1
    mycursor.execute(sql, val)
    mydb.commit()