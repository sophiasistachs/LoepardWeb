import sqlite3

# database file connection 
database = sqlite3.connect("Instuctor.db") 
  
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 
  
# SQL command to create a table in the database 
sql_command = """CREATE TABLE INSTRUCTOR (  
ID INTEGER PRIMARY KEY NOT NULL,
FIRST NAME TEXT NOT NULL,
SURNAME TEXT NOT NULL, 
YEAR OF HIRE NOT NULL, 
DEPARTMENT NOT NULL,
EMAIL NOT NULL)
;"""
  
# execute the statement 
cursor.execute(sql_command) 
  
# SQL command to insert the data in the table, must be done one at a time 
sql_command = """INSERT INTO INSTRUCTOR VALUES( 20001, 'JOSEPH', 'FOURIER', 1820, 'BSEE', 'FOURIERJ');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO INSTRUCTOR VALUES( 20002, 'NELSON', 'PATRICK', 1994, 'HUSS', 'PATRICKN');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO INSTRUCTOR VALUES( 20003, 'GALILEO', 'GALILEI', 1600, 'BSAS', 'GALILEIG');"""
cursor.execute(sql_command) 
               
sql_command = """INSERT INTO INSTRUCTOR VALUES( 20004, 'ALAN', 'TURING', 1940, 'BSCO', 'TURINGA');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO INSTRUCTOR VALUES( 20005, 'KATIE', 'BOUUMAN', 2019, 'BCOS', 'BOUMANK');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO INSTRUCTOR VALUES( 20006, 'DANIEL', 'BERNOULLI', 1760, 'BSME', 'BERNOULLID');"""
cursor.execute(sql_command) 

# QUERY FOR ALL
print("Entire table")
cursor.execute("""SELECT * FROM INSTRUCTOR""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)


# # QUERY FOR SOME
# print("Only those born prior to 1950")
# cursor.execute("""SELECT * FROM INSTRUCTOR  < 1950""")
# query_result = cursor.fetchall()

# for i in query_result:
# 	print(i)

# ADDING FROM USER INPUT
# uid = input ("ID of instructor: ")
# fname = input("First name of instructor: ")
# lname = input("Last name of instructor: ")
# hireyear = input("Hire year of instructor: ") 
# dept = input("Department of instructor: ") 
# emial = input("Email of instructor: ") 

# ADDING FROM USER INPUT
uid = input ("ID of instructor: ")	

sql_command = """DELETE FROM INSTRUCTOR WHERE ID = """ + str(uid)
cursor.execute(sql_command)

print("Entire table")
cursor.execute("""SELECT * FROM INSTRUCTOR""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)

# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
database.commit() 
  
# close the connection 
database.close() 
