import sqlite3

# database file connection 
database = sqlite3.connect("Admin.db") 
  
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 
  
# SQL command to create a table in the database 
# sql_command = """CREATE TABLE ADMIN (  
# ID INTEGER PRIMARY KEY NOT NULL,
# NAME TEXT NOT NULL,
# SURNAME TEXT NOT NULL,
# TITLE TEXT NOT NULL,
# OFFICE TEXT NOT NULL,
# EMAIL TEXT NOT NULL)
# ;"""
  
# # execute the statement 
# cursor.execute(sql_command) 
  
# SQL command to insert the data in the table, must be done one at a time 
# sql_command = """INSERT ADMIN VALUES(30001, 'MARGRET', 'HAMILTON', 'PRESIDENT', 'DOBBS 1600', 'hamiltonm');"""
# cursor.execute(sql_command) 

sql_command = """UPDATE Admin
SET TITLE = 'Vice President', EMAIL = 'rubinv'
WHERE ID = 30002;"""
cursor.execute(sql_command) 


# QUERY FOR ALL
print("Entire table")
cursor.execute("""SELECT * FROM ADMIN""")
query_result = cursor.fetchall()
  
for i in query_result:
	print(i)


# # QUERY FOR SOME
# print("Only those born prior to 1950")
# cursor.execute("""SELECT * FROM PROGRAMMER WHERE BIRTHYEAR < 1950""")
# query_result = cursor.fetchall()

# for i in query_result:
# 	print(i)

# # ADDING FROM USER INPUT
# uid = "6"
# fname = input("First name of a famous programmer: ")
# lname = input("Last name of the same programmer: ")
# birthyear = input("Birth year of the same programmer: ") 

# cursor.execute("""INSERT INTO PROGRAMMER VALUES('%s', '%s', '%s', '%s');""" % (uid, fname, lname, birthyear))

# print("Entire table")
# cursor.execute("""SELECT * FROM PROGRAMMER""")
# query_result = cursor.fetchall()
  
# for i in query_result:
# 	print(i)

# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
database.commit() 
  
# close the connection 
database.close() 
