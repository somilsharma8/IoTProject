import sqlite3

def createTable():
	connection=sqlite3.connect("login.db")
	
	#connection.execute("CREATE TABLE USERS (USERNAME TEXT NOT NULL, EMAILID TEXT, PASSWORD TEXT)")
	#connection.execute("INSERT INTO USERS VALUES (?,?,?)", ('somilsharma8','somilsharma8@gmail.com','somilsharma'))
	#connection.commit()
	result = connection.execute("SELECT * FROM USERS")
	for data in result:
		print("Username: ",data[0])
		print("EMAILID: ", data[1])
		print("PASSWORD: ", data[2])
	
	connection.close()
		
createTable() 
