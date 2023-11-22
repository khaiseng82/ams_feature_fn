#importing required libraries
import mysql.connector



def dBConnect(Type ,Flow_Value, Pressure_Value, Temperature_Value, AccumFlow_Value, Status_Value, current_time):
	dataBase = mysql.connector.connect(
	    host = "localhost",
	    user = "root",
	    passwd = "12345678",
	    database = "amsdb"
	)
	 
	# preparing a cursor object
	cursorObject = dataBase.cursor()

	'''
	# creating database
	cursorObject.execute("CREATE DATABASE amsdb")
	'''
	  
	'''
	# creating table 
	amsTest = """CREATE TABLE AMSTEST (
	                   RC_CB  VARCHAR(50) NOT NULL,
	                   Description VARCHAR(50) NOT NULL,
	                   Value VARCHAR(50),
	                   SIunit VARCHAR(50) NOT NULL,
	                   Operating INT,
	                   Idle INT,
	                   Standby INT,
	                   Isolation INT,
	                   DateTimeStamp TIMESTAMP
	                   )"""
	  
	# table created
	cursorObject.execute(amsTest)   
	'''
	'''
	# creating table for machine learning
	amsData2 = """CREATE TABLE AMSDATA_2 (
	                   RC_CB  VARCHAR(50) NOT NULL,
	                   Air_Flow VARCHAR(50) NOT NULL,
	                   Pressure VARCHAR(50) NOT NULL,
	                   Temperature VARCHAR(50) NOT NULL,
	                   Accumulated_Flow VARCHAR(50) NOT NULL,
	                   Operating INT,
	                   Idle INT,
	                   Standby INT,
	                   Isolation INT,
	                   DateTimeStamp TIMESTAMP
	                   )"""
	  
	# table created
	cursorObject.execute(amsData2)   
	'''

	'''
	statusCheck(Status_Value)

	sql = "INSERT INTO AMSTEST (RC_CB, Description, Value, SIunit, Operating, Idle, Standby, Isolation, DateTimestamp)\
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = [(Type, "Air Flow", Flow_Value, "L/Min", OpVal, IdVal, StVal, IsVal, current_time),
	(Type, "Pressure", Pressure_Value, "kPa", OpVal, IdVal, StVal, IsVal, current_time),
	(Type, "Temperature", Temperature_Value/10, "°C", OpVal, IdVal, StVal, IsVal, current_time),
	(Type, "Accumulated Flow", AccumFlow_Value*10, "L", OpVal, IdVal, StVal, IsVal, current_time)]
	print(OpVal, IdVal, StVal, IsVal)
	   
	cursorObject.executemany(sql, val)

	# only commit when adding values
	dataBase.commit()
	'''


	
	# for machine learning
	statusCheck(Status_Value)

	sql = "INSERT INTO AMSDATA_2 (RC_CB, Air_Flow, Pressure, Temperature, Accumulated_Flow, Operating, Idle, Standby, Isolation, DateTimestamp)\
	VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s)"
	val = [(Type, Flow_Value, Pressure_Value, Temperature_Value/10, AccumFlow_Value*10, OpVal, IdVal, StVal, IsVal, current_time)]
	print(OpVal, IdVal, StVal, IsVal)
	   
	cursorObject.executemany(sql, val)

	# only commit when adding values
	dataBase.commit()
	

	# disconnecting from server
	dataBase.close()

def statusCheck(Status_Value):
	global OpVal
	global IdVal
	global StVal
	global IsVal
	OpVal = 0
	IdVal = 0
	StVal = 0
	IsVal = 0
	if (Status_Value == 1):
		OpVal = 1
	elif (Status_Value == 2):
		IdVal = 1
	elif (Status_Value == 3):
		StVal = 1
	elif (Status_Value == 4):
		IsVal = 1
	elif (Status_Value == 17):
		OpVal = 1
	elif (Status_Value == 19):
		StVal = 1
	elif (Status_Value == 20):
		IsVal = 1
	elif (Status_Value == 36):
		IsVal = 1