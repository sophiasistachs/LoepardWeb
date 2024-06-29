from pickle import FALSE
from re import S
import sqlite3
from statistics import quantiles
from random import randrange
from turtle import title

database = sqlite3.connect("Database.db")
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
  def setfirst(self, user):
    self.name = input("Please enter first name: ")
    sql_command = """UPDATE """ + user.upper() + """ SET NAME = """ + self.name + """ WHERE ID = """ + str(self.ID)
    cursor.execute(sql_command)
    database.commit();
    
  def setlast(self, user):
    self.surname = input("Please enter last name: ")
    sql_command = """UPDATE """ + user.upper() + """ SET SURNAME = """ + self.surname + """ WHERE ID = """ + str(self.ID)
    cursor.execute(sql_command)
    database.commit();

  def setid(self, user):
    self.ID = input("Please enter ID numbr: ")
    sql_command = """UPDATE """ + user.upper() + """ SET ID = """ + self.ID + """ WHERE NAME = """ + self.name + """, SURNAME = """ + self.surname
    cursor.execute(sql_command)
    database.commit();

  def showfirst(self):
    print(self.name)
    database.commit();

  def showlast(self):
    print(self.surname)
    database.commit();

  def showid(self):
    print(self.ID)
    database.commit();

#Student
class Student(User):
  
  courses = []

  #constructer
  def __init__(self, name, surname, ID):
    super().__init__(name, surname, ID)

  #Methods
  def searchcourse(self, course):
    course = course.upper()
    
    sql_command = """SELECT TITLE FROM COURSE WHERE TITLE = '%s'""" % (course)
    cursor.execute(sql_command)
    query_result = cursor.fetchall()
    
    if (len(query_result) > 0):
      return "Course Found"
    
    else:
      return "Course " + course + " does NOT Exist!!"

    database.commit();
    # try:
    #     sql_command = """SELECT TITLE FROM COURSE WHERE TITLE = '%s'""" % (course)
    #     cursor.execute(sql_command)
    #     query_result = cursor.fetchall
    #     return "Course " + query_result + " Found"
    # except:
    #   return "Course " + course + " does NOT Exist!!"

  def add_drop(self):
    
    ans = "Invalid Answer"
    while (ans == "Invalid Answer"):

        ans = input("Would you like to add or drop a course (select one): ").upper()
        if ans == "ADD":
          course = input("Please enter the name of the course you would like to add: ").upper()
          found = self.searchcourse(course)

          if (found == "Course Found"):
            self.courses.append(course)
            print(course + " was added to your lists of courses")
          else:
            print(found)
      
        elif ans == "DROP":
          if (len(self.courses) > 0):
              course = input("Please enter the name of the course you would like to drop: ").upper()
              if (course in self.courses):
                self.courses.remove(course)
                print("Course " + course + " was Removed from the List of Courses")
              else:
                print("Course NOT FOUND therefore could NOT be Removed From your List of Courses")

          else:
            print("No Courses can be Dropped as You are Not Registered for any Courses")
         
        else:
          ans = "Invalid Answer"
    
    database.commit();

  def show_schedule(self):
    print("Schedule:\n-------------------------------------")
    schedule = []
    
    if(len(self.courses) == 0):
      print("Empty Due to Not Being Enrolled in any Courses")
      
    else:
        for num in range(len(self.courses)):
          course = self.courses[num].upper()
          sql_command = """SELECT * FROM COURSE WHERE TITLE = '%s'""" % (course)
          cursor.execute(sql_command)
          query_result = cursor.fetchall()
          #Title, Department, Semester, Year, DayOfWeek, Time
          crn = query_result[0][0]
          title = query_result[0][1]
          dep = query_result[0][2]
          sem = query_result[0][4]
          year = query_result[0][5]
          dow = query_result[0][3]
          time = query_result[0][7]
          credit = query_result[0][6]
          schedule.append({title, dep, sem, year, dow, time})
          print(title + " at " + dep + " during " + sem + " " + str(year) + " " + dow + " at " + str(time) + "\n")
    
    database.commit();
           
#Instructor
class Instructor(User):
  ID = None
  courses = []

  #Constructer
  def __init__(self, name, surname, ID):
    super().__init__(name, surname, ID)
    self.courses = []

  #Methods
  def show_schedule(self):
    print("Schedule:\n-------------------------------------\n")
    schedule = []
    
    if(len(self.courses) == 0):
      print("Empty Due to Not Being Enrolled in any Courses")
     
    else:
      for num in range(len(self.courses)):
          course = self.courses[num][0]
          sql_command = """SELECT * FROM COURSE WHERE TITLE = '%s'""" % (course)
          cursor.execute(sql_command)
          query_result = cursor.fetchall()
          #Title, Department, Semester, Year, DayOfWeek, Time
          crn = query_result[0][0]
          title = query_result[0][1]
          dep = query_result[0][2]
          sem = query_result[0][4]
          year = query_result[0][5]
          dow = query_result[0][3]
          time = query_result[0][7]
          credit = query_result[0][6]
          schedule.append({title, dep, sem, year, dow, time})
          print(title + " at " + dep + " during " + sem + " " + str(year) + " " + dow + " at " + str(time) + "\n")
  
    database.commit();

  def show_classlist(self):
    print("Class List:\n-------------------------------------\n")
    for course in self.courses[0]:
      print(course + "\n")
   
    database.commit();
      
  def searchcourse(self, course):
    course = course.upper()
    try:
        sql_command = """SELECT TITLE FROM COURSE WHERE TITLE = '%s'""" % course
        cursor.execute(sql_command)
        return "Course Found"
    except:
      return "Course " + course + " does NOT Exist!!"
    
    database.commit();  

#Admin
class Admin(User):
  #Constructer
  def __init__(self, name, surname, ID):
    super().__init__(name, surname, ID)

  #Methods
  def sys_addCourse(self):
    working = False
    crn = input("Please enter the crn of the course you would like to add to the system: ")
    title = input("Please enter the name of the course: ").upper()
    department = input("Please enter the department of the course: ").upper()
    day = input("Please enter the day of the week the course will be aviable: ").upper()
    semester = input("Please enter the semester the course will be aviable: ").upper()
    year = input("Please enter the year the course will be aviable: ")
    credit = input("Please enter the number of credits the course is worth: ")
    time = input("Please enter the time the course will be taking place: ").upper()
    
    sql_command = """INSERT INTO COURSE VALUES ('%d', '%s', '%s', '%s', '%s', '%d', '%d', '%s');""" % (int(crn), title, department, day, semester, int(year), int(credit), time)

    cursor.execute(sql_command) 
    print(title + " was Added to the List of Available Courses")
    database.commit();

    sql_command = """ALTER TABLE STUDENT ADD COLUMN CRN_%s;""" % str(crn)
    cursor.execute(sql_command) 
    print("Student Table Altered")
    
    database.commit();

  def sys_dropCourse(self):
    course = input("Please enter the name of the course you would like to drop from the system: ").upper()
    sql_command = """DELETE * FROM COURSE WHERE TITLE = """ + course
    cursor.execute(sql_command)
    print(course + " was Deleted From the List of Avaliable Courses\n")
    database.commit();

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
        
    database.commit();

  def course_addremove_student(self):
    ans = input("Would you like to add or remove a student (select one):")
    student = input("Who is the student:")
    if ans == "add":
      course = input("Please enter the name of the course you would like to add the student to: ")
      print(student + " has been added to " + course )
    elif ans == "drop":
      course = input("Please enter the name of the course you would like to drop the student from: ")
      print(student + " has been dropped from" + course )
      
    database.commit();

  def course_roster(self):
      course = input("Please enter the course you would like the roster for:").upper()
      print("Here is the roster for course", course, "\n\nROSTER")
      database.commit();
  

#Login Page
#Check Using ID (Students > 10000; Instructors > 20000; Admin > 30000)
user = "Invalid Login!"
while (user == "Invalid Login!"):
    email = input("Enter your username (Email): ").upper()
    password =  input("Enter your password (case sensitive): ")
     
    sql_command = """SELECT ID, NAME, SURNAME FROM STUDENT WHERE EMAIL = '%s' AND PASSWORD = '%s'""" % (str(email), str(password))
    cursor.execute(sql_command) 
    query_result = cursor.fetchall()
    if (len(query_result) == 0):
       sql_command = """SELECT ID, FIRST, SURNAME FROM INSTRUCTOR WHERE EMAIL = '%s' AND PASSWORD = '%s'""" % (str(email), str(password))
       cursor.execute(sql_command)
       query_result = cursor.fetchall()
       if (len(query_result) == 0):
          sql_command = """SELECT ID,NAME, SURNAME FROM ADMIN WHERE EMAIL = '%s' AND PASSWORD = '%s'""" % (str(email), str(password))
          cursor.execute(sql_command)
          query_result = cursor.fetchall()
          if (len(query_result) == 0):
              print("\n" + user + " Try Again:\n")
              continue
          else:
                ID = query_result[0][0]
                name = query_result[0][1]
                surname = query_result[0][2]
                user = "Admin"
                break
       else:
            ID = query_result[0][0]
            name = query_result[0][1]
            surname = query_result[0][2]
            user = "Instructor"
            break
    else:
        ID = query_result[0][0]
        name = query_result[0][1]
        surname = query_result[0][2]
        user = "Student"
        break
  
#Student Methods
if user == "Student":
    print(name + " " + surname + " has been found.");

    p = Student(name, surname, ID) #creates student
    print("Student has been created with name", p.name, p.surname) #verifies student has been created

    task = "0"
    while task != "4": #While loop allows student to pick their availableactions and runs cooresponding method until they exit the program
        task = input("\nPlease select the number cooresponding with your desired action: \n 1)Search Courses \n 2)Add/Drop Course \n 3)Print Schedule \n 4)Logout \n")
        if task  ==  "1" :
          course = input("Enter a course you are seraching for: ")
          print(p.searchcourse(course))
        elif task ==  "2":
          p.add_drop()
        elif task == "3":
          p.show_schedule()
        elif task == "4":
          break
        else:
          print("\nNo option was chosen. Please select a choice:\n")  

#Instructor Methods
elif user == "Instructor":
    print(name + " " + surname + " has been found.");


    #creates Instructor
    p0 = Instructor(name, surname, ID) 
    print("Instructor has been created with name", p0.name, p0.surname)
    
    #Assigning Available Courses to Selected Instructor
    sql_command = """SELECT TITLE FROM COURSE"""
    cursor.execute(sql_command)
    query_result = cursor.fetchall()

    for i in range(ID % 10):
      p0.courses.append(query_result[randrange(len(query_result))])

    task = "0"
    while task != "5": #While loop allows Instructor to pick their available actions and runs cooresponding method until they exit the program
        task = input("\nPlease select the number cooresponding with your desired action: \n 1)Print Schedule \n 2)Print Classlist \n 3)Search for Courses \n 4)Assign one course to each instructor and search based on course \n 5)Logout \n")
        if task  ==  "1" :
          p0.show_schedule()
        elif task ==  "2":
          p0.show_classlist()
        elif task == "3":
          course = input("Enter a course you are seraching for: ")
          print(p0.searchcourse(course))
        elif task == "4":
          ######################################      Assign a Course to Each Instructor      ######################################  
            sql_command = """SELECT FIRST, SURNAME, ID FROM INSTRUCTOR"""
            cursor.execute(sql_command)
            query_result = cursor.fetchall()

            instructors = []
            for instructor in query_result:
              teach = Instructor(instructor[0], instructor[1], instructor[2])
              instructors.append(teach)


            #Match each course to an instructor
            sql_command = """SELECT * FROM COURSE"""
            cursor.execute(sql_command)
            query_result = cursor.fetchall()  
            for num in range(len(instructors)):
                      #Title, Department, Semester, Year, DayOfWeek, Time
                      crn = query_result[num][0]
                      title = query_result[num][1]
                      dep = query_result[num][2]
                      sem = query_result[num][4]
                      year = query_result[num][5]
                      dow = query_result[num][3]
                      time = query_result[num][7]
                      credit = query_result[num][6]
                      instructors[num].courses.append(title)
                      print(title + " at " + dep + " during " + sem + " " + str(year) + " " + dow + " at " + str(time) + " is taught by " + instructors[num].name + " " + instructors[num].surname+ "\n")
          
            sql_command = """SELECT TITLE, DEPARTMENT FROM COURSE"""
            cursor.execute(sql_command)
            query_result = cursor.fetchall()
            for i in query_result:
              print(i[0] + " is a course from the " + i[1] + " department")
  
            searching = "YES"
            while(searching == "YES"):
                course = input("\nEnter a course you would like to question for instructors: ")
                found = False
                i = 0
                while (found == False):
                  if (i == len(instructors)):
                    print("No Instructor is Assigned to this Course")
                    break
                  elif (instructors[i].courses[0] == course.upper()):
                    found = True
                    print(instructors[i].name + " " + instructors[i].surname + " is Assigned to Course " + course)
                    break
                  else:
                    i += 1
                searching = input("\nWould you like to search for the instructor of another course (yes or no)? ").upper()

            ######################################      Assign a Course to Each Instructor      ######################################
        elif task == "5":
          break
        else:
          print("\nNo option was chosen. Please select a choice:\n")

#Admin Methods
elif user == "Admin":
    print(name + " " + surname + " has been found.");


    #creates admin
    p1 = Admin(name, surname, id) 
    print("Admin has been created with name", p1.name, p1.surname) #verifies admin has been created

    task = "0"
    while task != "6": #While loop allows admin to pick their available actions and runs cooresponding method until they exit the program
        task = input("\nPlease select the number cooresponding with your desired action: \n 1)Add course to System \n 2)Remove course from system \n 3)Add/Remove user \n 4)Add/Remove student from course  \n 5)Search and Print Course Roster \n 6)Logout \n")
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
        elif task == "6":
          break
        else:
          print("\nNo option was chosen. Please select a choice:\n")  

#Close the connection 
database.commit();          
database.close()