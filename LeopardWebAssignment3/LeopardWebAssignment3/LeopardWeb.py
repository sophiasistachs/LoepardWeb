import sqlite3

# database file connection 
database = sqlite3.connect("LeopardWeb.db") 
  
# cursor objects are used to traverse, search, grab, etc. information from the database, similar to indices or pointers  
cursor = database.cursor() 
   
#Base Class
class User:
  #Attributes
  name = "default"
  surname = "default"
  ID = 0000

  #Constructer
  def __init__(self, name, surname, ID):
    self.name  = name
    self.surname = surname
    self.ID = ID

  #Methods
  def setfirst(self):
    self.name = input("Please enter first name: ")

  def setlast(self):
    self.surname = input("Please enter last name: ")

  def setid(self):
    self.ID = input("Please enter ID numbr: ")

  def showfirst(self):
    print(self.name)

  def showlast(self):
    print(self.surname)

  def showid(self):
    print(self.ID)

#Student
class Student(User):
  #constructer
  def __init__(self, name, surname, ID):
    super().__init__(name, surname, ID)

  #Methods
  def searchcourse(self):
    course = input("Please enter the name of the course you are searching for: ")
    print("Here are your results for course",course )

  def add_drop(self):
    ans = input("Would you like to add or drop a course (select one):")
    if ans == "add":
      course = input("Please enter the name of the course you would like to add: ")
      print("Course ", course, "has been added ")
    elif ans == "drop":
      course = input("Please enter the name of the course you would like to drop: ")
      print("Course ", course, "has been droped ")

  def show_schedule(self):
    print("Here is your schedule: \nSCHEDULE")

#Instructor
class Instructor(User):
  #Constructer
  def __init__(self, name, surname, ID):
    super().__init__(name, surname, ID)

  #Methods
  def show_schedule(self):
    print("Here is your Instructor schedule: \nSCHEDULE")

  def show_classlist(self):
    print("Here is your classlist: \nCLASSLIST")

  def searchcourse(self):
    course = input("Please enter the name of the course you are searching for: ")
    print("Here are your results for course",course )

#Admin
class Admin(User):
  #Constructer
  def __init__(self, name, surname, ID):
    super().__init__(name, surname, ID)

  #Methods
  def sys_addCourse(self):
    course = input("Please enter the name of the course you would like to add to the system: ")
    print("Course",course, "has been added to the system")

  def sys_dropCourse(self):
    course = input("Please enter the name of the course you would like to drop from the system: ")
    print("Course",course, "has been dropped to the system")

  def sys_addremove_user(self):
    ans = input("Would you like to add or remove a user (select one):")
    if ans == "add":
      course = input("Please enter the name of the user you would like to add: ")
      print("Course ", course, "has been added ")
    elif ans == "drop":
      course = input("Please enter the name of the user you would like to drop: ")
      print("Course ", course, "has been droped ")

  def course_addremove_student(self):
    ans = input("Would you like to add or remove a student (select one):")
    student = input("Who is the student:")
    if ans == "add":
      course = input("Please enter the name of the course you would like to add the student to: ")
      print(Student, "has been added to", course )
    elif ans == "drop":
      course = input("Please enter the name of the course you would like to drop the student from: ")
      print(Student, "has been dropped from", course )

  def course_roster(self):
      course = input("Please enter the course you would like the roster for:")
      print("Here is the roster for course", course, "\n\nROSTER")


name = input("Enter your username (Email): ")
ID =  int(input("Enter your password (ID): "))    

#Login Page
#Check Using ID (Students > 10000; Instructors > 20000; Admin > 30000)
if ID > 40000 and ID < 30000:
    user = "Admin" 
elif ID > 20000:
    user = "Instructor"
elif ID > 10000:
  user = "Student"
else:
  user = "Invalid ID!"

print(user)
database.close()

#Student Methods
if user == "Student":
    database = sqlite3.connect("Student.db")
    sql_command = """SELECT NAME AND SURNAME FROM STUDENT WHERE ID = """ + str(ID)
    cursor.execute(sql_command)
    query_result = cursor.fetchall()
    name = query_result[0]
    surname = query_result[1]
    print(name + " " + surname + " has been found.");

    p = Student(name, surname, ID) #creates student
    print("Student has been created with name", p.name, p.surname) #verifies student has been created

    task = "0"
    while task != "4": #While loop allows student to pick their availableactions and runs cooresponding method until they exit the program
        task = input("\nPlease select the number cooresponding with your desired action: \n 1)Search Courses \n 2)Add/Drop Course \n 3)Print Schedule \n 4)Exit \n")
        if task  ==  "1" :
          p.searchcourse()
        elif task ==  "2":
          p.add_drop()
        elif task == "3":
          p.show_schedule()





#Instructor Methods
elif user == "Instructor":
    database = sqlite3.connect("Instructor.db")
    sql_command = """SELECT NAME AND SURNAME FROM INSTRUCTOR WHERE ID = """ + str(ID)
    cursor.execute(sql_command)
    query_result = cursor.fetchall()
    query_result = cursor.fetchall()
    name = query_result[0]
    surname = query_result[1]
    print(name + " " + surname + " has been found.");



    p0 = Instructor(name, surname, ID) #creates Instructor
    print("Instructor has been created with name", p0.name, p0.surname) #verifies student has been created

    task = "0"
    while task != "4": #While loop allows Instructor to pick their available actions and runs cooresponding method until they exit the program
        task = input("\nPlease select the number cooresponding with your desired action: \n 1)Print Schedule \n 2)Print Classlist \n 3)Search for Courses \n 4)Exit \n")
        if task  ==  "1" :
          p0.show_schedule()
        elif task ==  "2":
          p0.show_classlist()
        elif task == "3":
          p0.searchcourse()



#Admin Methods
elif user == "Admin":
    database = sqlite3.connect("Admin.db")
    sql_command = """SELECT NAME AND SURNAME FROM ADMIN WHERE ID = """ + str(ID)
    cursor.execute(sql_command)
    query_result = cursor.fetchall()
    name = query_result[0]
    surname = query_result[1]
    print(name + " " + surname + " has been found.");



    p1 = Admin(name, surname, id) #creates admin
    print("admin has been created with name", p1.name, p1.surname) #verifies admin has been created

    task = "0"
    while task != "6": #While loop allows admin to pick their available actions and runs cooresponding method until they exit the program
        task = input("\nPlease select the number cooresponding with your desired action: \n 1)Add course to System \n 2)Remove course from system \n 3)Add/Remove user \n 4)Add/Remove student from course  \n 5)Search and Print Course Roster \n 6)Exit \n")
        if task  ==  "1" :
          p1.sys_addCourse()
        elif task ==  "2":
          p1.sys_dropCourse()
        elif task == "3":
          p1.sys_addremove_user()
        elif task == "4":
          p1.course_addremove_student()
        elif task == "5":
          p1.course_roster()

database.close()
database = sqlite3.connect("LeopardWeb.db")

# close the connection 
database.close() 







#REFERENCE CODE
#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#

# # QUERY FOR ALL
# print("Entire table")
# cursor.execute("""SELECT * FROM STUDENT""")
# query_result = cursor.fetchall()
  
# for i in query_result:
# 	print(i)

# # QUERY FOR SOME
# print("Only those born prior to 1950")
# cursor.execute("""SELECT * FROM PROGRAMMER WHERE BIRTHYEAR < 1950""")
# query_result = cursor.fetchall()

# for i in query_result:
# 	print(i)

# # ADDING FROM USER INPUT
# uid = "6"
# name = input("First name of a famous programmer: ")
# surname = input("Last name of the same programmer: ")
# birthyear = input("Birth year of the same programmer: ") 

# cursor.execute("""INSERT INTO PROGRAMMER VALUES('%s', '%s', '%s', '%s');""" % (uid, name, surname, birthyear))

# print("Entire table")
# cursor.execute("""SELECT * FROM PROGRAMMER""")
# query_result = cursor.fetchall()
  
# for i in query_result:
# 	print(i)

# To save the changes in the files. Never skip this.  
# If we skip this, nothing will be saved in the database. 
#database.commit() 

#\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\#