import sqlite3

# database file connection 
database = sqlite3.connect("Student.db") 
  
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 
  
# SQL command to create a table in the database 
sql_command = """CREATE TABLE STUDENT (  
ID INTEGER PRIMARY KEY NOT NULL,
NAME TEXT NOT NULL,
SURNAME TEXT NOT NULL,
GRADDATE INTEGER NOT NULL,
MAJOR TEXT NOT NULL,
EMAIL TEXT NOT NULL
)
;"""
  
# execute the statement 
cursor.execute(sql_command) 
  
# SQL command to insert the data in the table, must be done one at a time 
sql_command = """INSERT INTO STUDENT VALUES(10001, 'ISAAC', 'NEWTON', 1668, 'BSAS', 'NEWTONI');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10002, 'MARIE', 'CURIE', 1903, 'BSAS', 'CURIEM');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10003, 'NIKOLA', 'TESLA', 1878, 'BSEE', 'TELSAN');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10004, 'THOMAS', 'EDISON', 1879, 'BSEE', 'NOTCOOL');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10005, 'JOHN', 'VON NEUMANN', 1923, 'BSCO', 'VONNEUMANNJ');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10006, 'GRACE', 'HOPPER', 1928, 'BCOS', 'HOPPERG');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10007, 'MAE', 'JEMISON', 1981, 'BSCH', 'JEMISONM');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10008, 'MARK', 'DEAN', 1979, 'BSCO', 'DEANM');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10009, 'MICHAEL', 'FARADAY', 1812, 'BSAS', 'FARADAYM');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10010, 'ADA', 'LOVELACE', 1832, 'BCOS', 'LOVELACEA');"""
cursor.execute(sql_command) 

#2 Added Students
sql_command = """INSERT INTO STUDENT VALUES(10011, 'CLARISSA', 'FAIRCHILD', 2005, 'BSAS', 'FAIRCLARY');"""
cursor.execute(sql_command) 

sql_command = """INSERT INTO STUDENT VALUES(10012, 'AMERICA', 'SINGER', 1869, 'BSEE', 'SINGERSELECTED');"""
cursor.execute(sql_command) 

#Save Table and Edits then Close the table
database.commit() 
database.close();
