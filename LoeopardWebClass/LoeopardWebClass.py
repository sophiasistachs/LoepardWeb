import sqlite3

# database file connection 
database = sqlite3.connect("LeoppardWebClass.db") 
  
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 
  
# SQL command to create a table in the database 
# sql_command = """CREATE TABLE CLASSES (  
# CRN INTEGER PRIMARY KEY NOT NULL,
# TITLE TEXT NOT NULL,
# DEPARTMENT TEXT NOT NULL, 
# DAYS OF THE WEEK TEXT NOT NULL, 
# SEMESTER TEXT NOT NULL,
# YEAR NOT NULL,
# CREDITS INTEGER NOT NULL,
# TIME NOT NULL
# )
# ;"""
  
# execute the statement 
#cursor.execute(sql_command) 
  
# SQL command to insert the data in the table, must be done one at a time 
# sql_command = """INSERT INTO CLASSES VALUES( 5650, 'Embedded Systems', 'ELEC', 'Monday and Wednesday' , 'Summer', 2024 , 4, '5:00 - 7:00');"""
# cursor.execute(sql_command) 

# sql_command = """INSERT INTO CLASSES VALUES( 3600, 'Signals and Systems', 'ELEC', 'Monday and Wednesday', 'Summer', 2024, 4, '10:00 - 12:00');"""
# cursor.execute(sql_command) 

# sql_command = """INSERT INTO CLASSES VALUES( 3225, 'Applied Programing', 'ELEC', 'Monday Tuesday Thursday' , 'Summer', 2024, 4, '8:00 - 10:00');"""
# cursor.execute(sql_command) 
               
# sql_command = """INSERT INTO CLASSES VALUES( 3550, 'Computer Networks', 'ELEC', 'Monday and Wednesday', 'Summer', 2024, 4, '12:30 - 2:00');"""
# cursor.execute(sql_command) 

# sql_command = """INSERT INTO CLASSES VALUES( 3200, 'Digital Circuits', 'ELEC', 'Wednesday and Friday' , 'Summer', 2024, 4, '8:00 - 9:00');"""
# cursor.execute(sql_command) 



# QUERY FOR ALL
print("Entire table")
cursor.execute("""SELECT * FROM CLASSES""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)


# # QUERY FOR SOME
# print("ELEC 3550")
# cursor.execute("""SELECT * FROM CLASSES   3550""")
# query_result = cursor.fetchall()

# for i in query_result:
print(i)

# ADDING FROM USER INPUT
crn = input ("CRN of Class: ")
title = input("Title of Class: ")
department = input("Department of Class: ")
daysofweek = input("Days of the Week: ") 
semester = input("Semester of Class: ") 
year = input("Year of Class: ") 
numcredits = input("Credits of Class: ") 
time = input("Time of Class: ") 

cursor.execute("""INSERT INTO CLASSES VALUES('%s', '%s', '%s', '%s', '%s', '%s','%s', '%s' );""" % (crn, title, department, daysofweek, semester, year, numcredits, time))

print("Entire table")
cursor.execute("""SELECT * FROM CLASSES""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)

# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
database.commit() 
  
# close the connection 
database.close() 

