import sqlite3
from statistics import quantiles


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
  def setfirst(self, user):
    self.name = input("Please enter first name: ")
    sql_command = """UPDATE """ + user.upper() + """ SET NAME = """ + self.name + """ WHERE ID = """ + str(self.ID)
    cursor.execute(sql_command)
    
  def setlast(self, user):
    self.surname = input("Please enter last name: ")
    sql_command = """UPDATE """ + user.upper() + """ SET SURNAME = """ + self.surname + """ WHERE ID = """ + str(self.ID)
    cursor.execute(sql_command)

  def setid(self, user):
    self.ID = input("Please enter ID numbr: ")
    sql_command = """UPDATE """ + user.upper() + """ SET ID = """ + self.ID + """ WHERE NAME = """ + self.name + """, SURNAME = """ + self.surname
    cursor.execute(sql_command)

  def showfirst(self):
    print(self.name)

  def showlast(self):
    print(self.surname)

  def showid(self):
    print(self.ID)

#Student
class Student(User):
  #constructer
  def __init__(self, name, surname, ID, courses = []):
    super().__init__(name, surname, ID)

  #Methods
  def searchcourse(self, course):
    course = course.upper()
    try:
        sql_command = """SELECT TITLE FROM CLASSES WHERE TITLE = """ + course
        cursor.execute(sql_command)
        return "Course Found"
    except:
      return "Course does NOT Exist!!"

  def add_drop(self):
    ans = input("Would you like to add or drop a course (select one):").upper()
    if ans == "add":
      course = input("Please enter the name of the course you would like to add: ")
      found = self.searchcourse(course)

      if (found == "Course Found"):
        self.courses.append(course)
        print(course + " was added to your lists of courses")
      else:
        print(found)
      
    elif ans == "drop":
      course = input("Please enter the name of the course you would like to drop: ")
      found = self.searchcourse(course)

      if (found == "Course Found"):
        self.courses.remove(course)
        print(course + " was removed to your lists of courses")
      else:
        print(found + " Therefore could NOT be Removed From your List of Courses")

  def show_schedule(self):
    print("Schedule:\n-------------------------------------")
    schedule = []
    
    if(len(self.courses) == 0):
      print("Empty Due to Not Being Enrolled in any Courses")
      
    else:
        for num in len(self.courses):
          sql_command = """SELECT * FROM CLASSES WHERE TITLE = """ + self.courses[num]
          cursor.execute(sql_command)
          query_result = cursor.fetchall()
          #Title, Department, Semester, Year, DayOfWeek, Time
          schedule[num] = [query_result[1], query_result[2], query_result[5], query_result[6], query_result[4], query_result[3]]
          print(schedule[num][0] + " at " + schedule[num][1] + " during " + schedule[num][2] + " " + schedule[num][3] + " " + schedule[num][4] + " at " + schedule[num][5])
           
#Instructor
class Instructor(User):
  #Constructer
  def __init__(self, name, surname, ID, courses = []):
    super().__init__(name, surname, ID)

  #Methods
  def show_schedule(self):
    print("Schedule:\n-------------------------------------\n")
    schedule = []
    
    if(len(self.courses) == 0):
      print("Empty Due to Not Being Enrolled in any Courses")
     
    else:
      for num in len(self.courses):
          sql_command = """SELECT * FROM CLASSES WHERE TITLE = """ + self.courses[num].upper()
          cursor.execute(sql_command)
          query_result = cursor.fetchall()
          #Title, Department, Semester, Year, DayOfWeek, Time
          schedule[num] = [query_result[1], query_result[2], query_result[5], query_result[6], query_result[4], query_result[3]]
          print(schedule[num][0] + " at " + schedule[num][1] + " during " + schedule[num][2] + " " + schedule[num][3] + " " + schedule[num][4] + " at " + schedule[num][5] + "\n")
  
  def show_classlist(self):
    print("Class List:\n-------------------------------------\n")
    for course in self.courses:
      print(course + "\n")
      
  def searchcourse(self, course):
    course = course.upper()
    try:
        sql_command = """SELECT TITLE FROM CLASSES WHERE TITLE = """ + course
        cursor.execute(sql_command)
        return "Course Found"
    except:
      return "Course does NOT Exist!!"

#Admin
class Admin(User):
  #Constructer
  def __init__(self, name, surname, ID):
    super().__init__(name, surname, ID)

  #Methods
  def sys_addCourse(self):
    crn = input("Please enter the crn of the course you would like to add to the system: ").upper()
    title = input("Please enter the name of the course: ").upper()
    department = input("Please enter the department of the course: ").upper()
    time = input("Please enter the time the course will be taking place: ").upper()
    day = input("Please enter the day of the week the course will be aviable: ").upper()
    semester = input("Please enter the semester the course will be aviable: ").upper()
    year = input("Please enter the year the course will be aviable: ").upper()
    credit = input("Please enter the number of credits the course is worth: ").upper()
    
    sql_command = """INSERT INTO CLASSES VALUES(""" + crn + """, """ + title + """, """ + department + """, """ + time + """, """ + day + """, """ + semester + """, """ + year + """, """ + credit + """);"""
    cursor.execute(sql_command) 
    print(title + " was Added to the List of Available Courses")

  def sys_dropCourse(self):
    course = input("Please enter the name of the course you would like to drop from the system: ").upper()
    sql_command = """DELETE * FROM CLASSES WHERE TITLE = """ + course
    cursor.execute(sql_command)
    print(course + " was Deleted From the List of Avaliable Courses\n")

  def sys_addremove_user(self):
    ans = input("Would you like to add or remove a user (select one):").upper()
    if ans == "add":
      ID = input("Please enter the ID of the user you would like to add: ")
      if ID > 40000 and ID < 30000:
        name = input("Enter new user's name: ")
        surname = input("Enter new Admin's surname: ")
        title = input("Enter new Admin's title: ")
        office = input("Enter new Admin's office: ")
        email = input("Enter new Admin's email: ")
        
        sql_command = """INSERT INTO ADMIN VALUES(""" + ID + """, """ + name + """, """ + surname + """, """ + title + """, """ + office + """, """ + email + """);"""
        cursor.execute(sql_command)
        
      elif ID > 20000:
        name = input("Enter new Instructor's name: ")
        surname = input("Enter new Instructor's surname: ")
        title = input("Enter new Instructor's title: ")
        hireYear = input("Enter new Instructor's year of hire: ")
        department = input("Enter new Instructor's department: ")
        email = input("Enter new Instructor's email: ")

        sql_command = """INSERT INTO INSTRUCTOR VALUES(""" + ID + """, """ + name + """, """ + surname + """, """ + title + """, """ + hireYear + """, """ + department + """, """ + email + """);"""
        cursor.execute(sql_command) 
        
      elif ID > 10000:
        name = input("Enter new Student's name: ")
        surname = input("Enter new Student's surname: ")
        gradYear = input("Enter new Student's expected graduation year: ")
        major = input("Enter new Student's major: ")
        email = input("Enter new Student's email: ")

        sql_command = """INSERT INTO STUDENT VALUES(""" + ID + """, """ + name + """, """ + surname + """, """ + gradYear + """, """ + major + """, """ + email + """);"""
        cursor.execute(sql_command) 
        
      else:
        print("Invalid ID! No User was Removed Due to no User being Selected")
         
    elif ans == "drop":
      ID = input("Please enter the ID of the user you would like to drop: ")
      if ID > 40000 and ID < 30000:
        sql_command = """DELETE * FROM ADMIN WHERE ID = """ + ID
        cursor.execute(sql_command)
      elif ID > 20000:
        sql_command = """DELETE * FROM INSTRUCTOR WHERE ID = """ + ID
        cursor.execute(sql_command)
      elif ID > 10000:
        sql_command = """DELETE * FROM STUDENT WHERE ID = """ + ID
        cursor.execute(sql_command)
      else:
        print("Invalid ID! No User was Removed Due to no User being Selected")

  def course_addremove_student(self):
    ans = input("Would you like to add or remove a student (select one):")
    student = input("Who is the student:")
    if ans == "add":
      course = input("Please enter the name of the course you would like to add the student to: ")
      print(student + " has been added to " + course )
    elif ans == "drop":
      course = input("Please enter the name of the course you would like to drop the student from: ")
      print(student + " has been dropped from" + course )

  def course_roster(self):
      course = input("Please enter the course you would like the roster for:").upper()
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

#Student Methods
if user == "Student":
    database = sqlite3.connect("Student.db")
    cursor = database.cursor()
    sql_command = """SELECT NAME, SURNAME FROM STUDENT WHERE ID = """ + str(ID)
    cursor.execute(sql_command)
    query_result = cursor.fetchall()
    name = query_result[0][0]
    surname = query_result[0][1]
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
    cursor = database.cursor()
    sql_command = """SELECT NAME, SURNAME FROM INSTRUCTOR WHERE ID = """ + str(ID)
    cursor.execute(sql_command)
    query_result = cursor.fetchall()
    query_result = cursor.fetchall()
    name = query_result[0][0]
    surname = query_result[0][1]
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
    cursor = database.cursor()
    sql_command = """SELECT NAME, SURNAME FROM ADMIN WHERE ID = """ + str(ID)
    cursor.execute(sql_command)
    query_result = cursor.fetchall()
    name = query_result[0][0]
    surname = query_result[0][1]
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

#Close the connection 
database.close()