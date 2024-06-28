import sqlite3

# database file connection 
database = sqlite3.connect("Database.db") 
  
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 
  
############################################################################################    STUDENT TABLE   ############################################################################################

# SQL command to create a table in the database 
sql_command = """CREATE TABLE STUDENT (  
ID INTEGER PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
SURNAME TEXT NOT NULL,
GRADDATE INTEGER NOT NULL,
MAJOR TEXT NOT NULL,
EMAIL TEXT NOT NULL,
PASSWORD TEXT NOT NULL
);"""
  
# execute the statement 
cursor.execute(sql_command) 
  
# SQL command to insert the data in the table, must be done one at a time 
sql_command = """INSERT INTO STUDENT VALUES(10001, 'ISAAC', 'NEWTON', 1668, 'BSAS', 'NEWTONI', 'pass1');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10002, 'MARIE', 'CURIE', 1903, 'BSAS', 'CURIEM', 'pass2');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10003, 'NIKOLA', 'TESLA', 1878, 'BSEE', 'TELSAN', 'pass3');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10004, 'THOMAS', 'EDISON', 1879, 'BSEE', 'NOTCOOL', 'pass4');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10005, 'JOHN', 'VON NEUMANN', 1923, 'BSCO', 'VONNEUMANNJ', 'pass5');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10006, 'GRACE', 'HOPPER', 1928, 'BCOS', 'HOPPERG', 'pass6');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10007, 'MAE', 'JEMISON', 1981, 'BSCH', 'JEMISONM', 'pass7');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10008, 'MARK', 'DEAN', 1979, 'BSCO', 'DEANM', 'pass8');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10009, 'MICHAEL', 'FARADAY', 1812, 'BSAS', 'FARADAYM', 'pass9');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10010, 'ADA', 'LOVELACE', 1832, 'BCOS', 'LOVELACEA', 'pass10');"""
cursor.execute(sql_command) 

#See Current Table
print("Student Table")
cursor.execute("""SELECT * FROM STUDENT""")
query_result = cursor.fetchall()
for i in query_result:
	print(i)

print("\n\n")

#2 Added Students
print("Add in a student:\n")
id = input("Enter ID: ")
name = input("Enter First Name: ").upper()
surname = input("Enter Surname: ").upper()
gradYear = input("Enter Expected Graduation Year: ")
major = input("Enter Major: ").upper()
email = input("Enter Email: ").upper()
password = input("Enter Password: ").upper()

sql_command = """INSERT INTO STUDENT VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % (str(id), name, surname, gradYear, major, email, str(password))
cursor.execute(sql_command) 

print("\nAdd in another student:\n")
id = input("Enter ID: ")
name = input("Enter First Name: ").upper()
surname = input("Enter Surname: ").upper()
gradYear = input("Enter Expected Graduation Year: ")
major = input("Enter Major: ").upper()
email = input("Enter Email: ").upper()
password = input("Enter Password: ").upper()

sql_command = """INSERT INTO STUDENT VALUES('%s', '%s', '%s', '%s', '%s', '%s', '%s');""" % (str(id), name, surname, gradYear, major, email, str(password))
cursor.execute(sql_command) 

#View Updated Table
sql_command = """SELECT * FROM STUDENT"""
cursor.execute(sql_command)
query_result = cursor.fetchall()
  
print("\nUpdated Student Table\n--------------------------------")
for i in query_result:
	print(i)

print("\n\n")
############################################################################################    STUDENT TABLE   ############################################################################################


############################################################################################    INSTRUCTOR TABLE   ############################################################################################



sql_command = """CREATE TABLE INSTRUCTOR (  
ID INTEGER PRIMARY KEY NOT NULL,
FIRST NAME TEXT NOT NULL,
SURNAME TEXT NOT NULL, 
YEAR OF HIRE NOT NULL, 
DEPARTMENT NOT NULL,
EMAIL NOT NULL,
PASSWORD TEXT NOT NULL
);"""
   
cursor.execute(sql_command) 
  
# SQL command to insert the data in the table, must be done one at a time 
sql_command = """INSERT INTO INSTRUCTOR VALUES( 20001, 'JOSEPH', 'FOURIER', 1820, 'BSEE', 'FOURIERJ', 'pass20');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO INSTRUCTOR VALUES( 20002, 'NELSON', 'PATRICK', 1994, 'HUSS', 'PATRICKN', 'pass21');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO INSTRUCTOR VALUES( 20003, 'GALILEO', 'GALILEI', 1600, 'BSAS', 'GALILEIG', 'pass22');"""
cursor.execute(sql_command) 
               
sql_command = """INSERT INTO INSTRUCTOR VALUES( 20004, 'ALAN', 'TURING', 1940, 'BSCO', 'TURINGA', 'pass23');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO INSTRUCTOR VALUES( 20005, 'KATIE', 'BOUUMAN', 2019, 'BCOS', 'BOUMANK', 'pass24');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO INSTRUCTOR VALUES( 20006, 'DANIEL', 'BERNOULLI', 1760, 'BSME', 'BERNOULLID', 'pass25');"""
cursor.execute(sql_command) 

# View Current Table
print("Instuctor Table")
cursor.execute("""SELECT * FROM INSTRUCTOR""")
query_result = cursor.fetchall()
for i in query_result:
	print(i)

# DELETING FROM USER INPUT
uid = input ("\n\nEnter the ID of the Instructor you Wish to Remove: ")	

sql_command = """DELETE FROM INSTRUCTOR WHERE ID = """ + str(uid)
cursor.execute(sql_command)

#View Updated Table
sql_command = """SELECT * FROM INSTRUCTOR"""
cursor.execute(sql_command)
query_result = cursor.fetchall()
  
print("Updated Instructor Table\n--------------------------------")
for i in query_result:
	print(i)


print("\n\n")

############################################################################################    INSTRUCTOR TABLE   ############################################################################################


############################################################################################    ADMIN TABLE   ############################################################################################


#SQL command to create a table in the database 
sql_command = """CREATE TABLE ADMIN (  
ID INTEGER PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
SURNAME TEXT NOT NULL,
TITLE TEXT NOT NULL,
OFFICE TEXT NOT NULL,
EMAIL TEXT NOT NULL,
PASSWORD TEXT NOT NULL
);"""
  
cursor.execute(sql_command) 
  
# SQL command to insert the data in the table, must be done one at a time 
sql_command = """INSERT INTO ADMIN VALUES( 30001, 'MARGRET', 'HAMILTON', 'PRESIDENT', 'DOBBS 1600', 'HAMILTONM', 'pass31');"""
cursor.execute(sql_command) 
sql_command = """INSERT INTO ADMIN VALUES( 30002, 'VERA', 'RUBIN', 'REGISTAR', 'WENTWORTH 101', 'RUBINV', 'pass32');"""
cursor.execute(sql_command) 

#View Admin Table
print("Admin Table")
cursor.execute("""SELECT * FROM ADMIN""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)

title = "VICE PRESIDENT"
id = str(30002)

print("Admin with ID = " + id + " is having their inofrmation updated.\nNew title is " + title + "\n")

sql_command = """UPDATE ADMIN SET TITLE = '%s' WHERE ID = '%s';""" % (title, id)
cursor.execute(sql_command) 


#View Updated Table
print("Updated Admin Table")
cursor.execute("""SELECT * FROM ADMIN""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)

print("\n\n")

############################################################################################    ADMIN TABLE   ############################################################################################



############################################################################################    COURSE TABLE   ############################################################################################

#SQL command to create a table in the database 
sql_command = """CREATE TABLE COURSE (  
CRN INTEGER PRIMARY KEY NOT NULL,
TITLE TEXT NOT NULL,
DEPARTMENT TEXT NOT NULL, 
DAYS OF THE WEEK TEXT NOT NULL, 
SEMESTER TEXT NOT NULL,
YEAR INTEGER NOT NULL,
CREDITS INTEGER NOT NULL,
TIME TEXT NOT NULL
)
;"""
  
cursor.execute(sql_command) 
  
#SQL command to insert the data in the table, must be done one at a time 
sql_command = """INSERT INTO COURSE VALUES( 5650, 'EMBEDDED SYSTEMS', 'ELEC', 'MONDAY WEDNESDAY' , 'SUMMER', 2024 , 4, '5:00-7:00');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO COURSE VALUES( 3600, 'SIGNALS AND SYSTEMS', 'ELEC', 'MONDAY WEDNESDAY', 'FALL', 2000, 2, '10:00-12:00');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO COURSE VALUES( 3225, 'APPLIED PROGRAMMING', 'ELEC', 'MONDAY TUESDAY THURSDAY' , 'WINTER', 1980, 4, '8:00-10:00');"""
cursor.execute(sql_command) 
               
sql_command = """INSERT INTO COURSE VALUES( 3550, 'COMPUTER NETWORKS', 'ELEC', 'MONDAY WEDNESDAY', 'SUMMER', 2024, 3, '12:30-2:00');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO COURSE VALUES( 3200, 'DIGITAL CIRCUITS', 'ELEC', 'WEDNESDAY FRIDAY' , 'WINTER', 1820, 4, '8:00-9:00');"""
cursor.execute(sql_command) 


# View Current Table
print("Course Table")
cursor.execute("""SELECT * FROM COURSE""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)


# ADDING FROM USER INPUT
print("\nCreating a New Course:\n")	
crn = input ("Enter CRN of Course: ")
title = input("Enter Title of Course: ").upper()
department = input("Enter Department of Course: ").upper()
daysofweek = input("Enter Days of the Week: ") .upper()
semester = input("Enter Semester of Course: ") .upper()
year = input("Enter Year of Course: ") 
numcredits = input("Enter Credits of Course: ") 
time = input("Enter Time of Course: ") 

cursor.execute("""INSERT INTO COURSE VALUES('%s', '%s', '%s', '%s', '%s', '%s','%s', '%s' );""" % (crn, title, department, daysofweek, semester, year, numcredits, time))

#View Updated Table
print("\nCourse Table")
cursor.execute("""SELECT * FROM COURSE""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)
############################################################################################    COURSE TABLE   ############################################################################################



#Save Table and Edits then Close the table
database.commit() 
database.close();