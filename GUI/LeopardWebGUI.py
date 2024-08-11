import tkinter as tk
from tkinter import * 
from tkinter.ttk import *
from tkinter import messagebox
import sqlite3

#Database initialization
database = sqlite3.connect("Database.db")
cursor = database.cursor()

#Window
root = Tk()
root.geometry("900x700")
root.title("Leopard Web")

def sequence(*functions):
    def func(*args, **kwargs):
        return_value = None
        for function in functions:
            return_value = function(*args, **kwargs)
        return return_value
    return func

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
    database.commit()
    
  def setlast(self, user):
    self.surname = input("Please enter last name: ")
    sql_command = """UPDATE """ + user.upper() + """ SET SURNAME = """ + self.surname + """ WHERE ID = """ + str(self.ID)
    cursor.execute(sql_command)
    database.commit()

  def setid(self, user):
    self.ID = input("Please enter ID numbr: ")
    sql_command = """UPDATE """ + user.upper() + """ SET ID = """ + self.ID + """ WHERE NAME = """ + self.name + """, SURNAME = """ + self.surname
    cursor.execute(sql_command)
    database.commit()

  def showfirst(self):
    print(self.name)
    database.commit()

  def showlast(self):
    print(self.surname)
    database.commit()

  def showid(self):
    print(self.ID)
    database.commit()

#Student
class Student(User):
  
  courses = []

  #constructer
  def __init__(self, name, surname, ID):
    super().__init__(name, surname, ID)

  #Methods
  def searchcourse(self):
    root.title("Student Search Course Screen")
    StudentSearchCourseFrame = tk.Frame(root, padx=20,pady=20)
    StudentSearchCourseFrame.pack(fill = "both", expand= True)

    def Logout(event=None):
        StudentSearchCourseFrame.pack_forget()
        root.bind('<Return>', enter)
        StudentWindow(self.ID, self.name, self.surname)

    def search(event=None):
        course = CourseTextBox.get().upper()
        if (len(course) > 0):
            sql_command = """SELECT TITLE FROM COURSE WHERE TITLE = '%s'""" % (course)
            cursor.execute(sql_command)
            query_result = cursor.fetchall()

            if (len(query_result) > 0):
                result = "Course " + course + " Found"
                ResultLabel = Label(StudentSearchCourseFrame, text = result, font='20')
                ResultLabel.place(relx = 0.5, rely = 0.2, anchor = CENTER, height=50, width=500)

            else:
                result = "Course " + course + " does NOT Exist!!"
                ResultLabel = Label(StudentSearchCourseFrame, text = result, font='20')
                ResultLabel.place(relx = 0.5, rely = 0.2, anchor = CENTER, height=50, width=500)

        else:
           messagebox.showwarning("Invalid Entry", "No Course was Entered to Search For!!")


    CourseLabel = Label(StudentSearchCourseFrame, text = "Please Enter a Course You Would Like to Search For:", font='20')
    CourseLabel.place(relx = 0.5, rely = 0.33, anchor = CENTER, height=50, width=500)

    CourseTextBox = tk.Entry(StudentSearchCourseFrame, font='30')
    CourseTextBox.place(relx = 0.5, rely = 0.4, anchor = CENTER, height=50, width=500)
    
    SearchButton = tk.Button(StudentSearchCourseFrame, text = "Search", height=2, width=15, font='30', command=search)
    SearchButton.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    root.bind('<Return>', search)

    LogoutButton = tk.Button(StudentSearchCourseFrame, text = "Logout", height=2, width=15, font='30', command=Logout)
    LogoutButton.place(relx = 0.5, rely = 0.8, anchor = CENTER)
    
  def addcourse(self):
    course = input("Please enter the name of the course you would like to add: ").upper()
    found = self.searchcourse(course)

    if (found == "Course Found"):
        self.courses.append(course)
        print(course + " was added to your lists of courses")
    else:
        print(found)

    
    database.commit()

  def dropcourse(self):
    if (len(self.courses) > 0):
        course = input("Please enter the name of the course you would like to drop: ").upper()
        if (course in self.courses):
            self.courses.remove(course)
            print("Course " + course + " was Removed from the List of Courses")
        else:
            print("Course NOT FOUND therefore could NOT be Removed From your List of Courses")
    else:
        print("No Courses can be Dropped as You are Not Registered for any Courses")
    database.commit()

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
    
    database.commit()
           
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
  
    database.commit()

#SOPHIA PUGA GET TO WORK ON THIS FUNCTION!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!!
#QUERY DATABASE FOR INCTRUCTOR NAME    
  def show_classlist(self):
    print("Class List:\n-------------------------------------\n")
    
    if (self.course.length != 0):
        for course in self.courses[0]:
          print(course + "\n")
    else:
       print("No courses found")

    database.commit();
      
  def searchcourse(self):
    root.title("Instructor Search Course Screen")
    InstructorSearchCourseFrame = tk.Frame(root, padx=20,pady=20)
    InstructorSearchCourseFrame.pack(fill = "both", expand= True)

    def Logout(event=None):
        InstructorSearchCourseFrame.pack_forget()
        root.bind('<Return>', enter)
        InstructorWindow(self.ID, self.name, self.surname)

    def search(event=None):
        course = CourseTextBox.get().upper()
        if (len(course) > 0):
            sql_command = """SELECT TITLE FROM COURSE WHERE TITLE = '%s'""" % (course)
            cursor.execute(sql_command)
            query_result = cursor.fetchall()

            if (len(query_result) > 0):
                result = "Course " + course + " Found"
                ResultLabel = Label(InstructorSearchCourseFrame, text = result, font='20')
                ResultLabel.place(relx = 0.5, rely = 0.2, anchor = CENTER, height=50, width=500)

            else:
                result = "Course " + course + " does NOT Exist!!"
                ResultLabel = Label(InstructorSearchCourseFrame, text = result, font='20')
                ResultLabel.place(relx = 0.5, rely = 0.2, anchor = CENTER, height=50, width=500)

        else:
           messagebox.showwarning("Invalid Entry", "No Course was Entered to Search For!!")


    CourseLabel = Label(InstructorSearchCourseFrame, text = "Please Enter a Course You Would Like to Search For:", font='20')
    CourseLabel.place(relx = 0.5, rely = 0.33, anchor = CENTER, height=50, width=500)

    CourseTextBox = tk.Entry(InstructorSearchCourseFrame, font='30')
    CourseTextBox.place(relx = 0.5, rely = 0.4, anchor = CENTER, height=50, width=500)
    
    SearchButton = tk.Button(InstructorSearchCourseFrame, text = "Search", height=2, width=15, font='30', command=search)
    SearchButton.place(relx = 0.5, rely = 0.6, anchor = CENTER)
    root.bind('<Return>', search)

    LogoutButton = tk.Button(InstructorSearchCourseFrame, text = "Logout", height=2, width=15, font='30', command=Logout)
    LogoutButton.place(relx = 0.5, rely = 0.8, anchor = CENTER)

#Admin
class Admin(User):
  #Constructer
  def __init__(self, name, surname, ID):
    super().__init__(name, surname, ID)

  #Methods
  # def sys_addCourse(self):
  #   working = False
  #   crn = input("Please enter the crn of the course you would like to add to the system: ")
  #   title = input("Please enter the name of the course: ").upper()
  #   department = input("Please enter the department of the course: ").upper()
  #   day = input("Please enter the day of the week the course will be aviable: ").upper()
  #   semester = input("Please enter the semester the course will be aviable: ").upper()
  #   year = input("Please enter the year the course will be aviable: ")
  #   credit = input("Please enter the number of credits the course is worth: ")
  #   time = input("Please enter the time the course will be taking place: ").upper()
    
  #   sql_command = """INSERT INTO COURSE VALUES ('%d', '%s', '%s', '%s', '%s', '%d', '%d', '%s');""" % (int(crn), title, department, day, semester, int(year), int(credit), time)

  #   cursor.execute(sql_command) 
  #   print(title + " was Added to the List of Available Courses")
  #   database.commit();

  #   sql_command = """ALTER TABLE STUDENT ADD COLUMN CRN_%s;""" % str(crn)
  #   cursor.execute(sql_command) 
  #   print("Student Table Altered")
    
  #   database.commit();

  def sys_addCourse(self):
    crn = int(crn)
    title = title.upper()
    department = department.upper()
    day = day.upper()
    semester = semester.upper()
    year = int(year)
    credit = int(credit)
    instructor = instructor.upper()

    working = False
    
    try:
      sql_command = """INSERT INTO COURSE VALUES (%d, '%s', '%s', '%s', '%s', %d, %d, '%s', '%s');""" % (crn, title, department, day, semester, year, credit, time, instructor)
      cursor.execute(sql_command) 
      database.commit()
      print(title + " was Added to the List of Available Courses")
    except:
      print("CRN already exists")

    try:
      sql_command = """ALTER TABLE STUDENT ADD COLUMN CRN_%s;""" % str(crn)
      cursor.execute(sql_command) 
      print("Student Table Altered")
      database.commit()
    except:
      print("CRN already exists")
  
    return "Course Added to Course Table. Course Column Added to Student Table."

  # def sys_dropCourse(self):
  #   crn = input("Please enter the CRN of the course you would like to drop from the system: ")
  #   sql_command = """DELETE FROM COURSE WHERE CRN = """ + crn
  #   cursor.execute(sql_command)
  #   database.commit();

  #   sql_command = """ALTER TABLE STUDENT DROP COLUMN CRN_%s;""" % str(crn)
  #   cursor.execute(sql_command)
  #   print("CRN_" + crn + " was Deleted From the List of Avaliable Courses\n")
  #   database.commit();

  def sys_dropCourse(self):
    try:
      sql_command = """DELETE FROM COURSE WHERE CRN = '%s';""" % (str(crn))
      cursor.execute(sql_command)
      database.commit()

      sql_command = """ALTER TABLE STUDENT DROP COLUMN CRN_%s;""" % (str(crn))
      print(sql_command)
      cursor.execute(sql_command)
      database.commit()
      return "CRN_" + str(crn) + " was Deleted From the List of Avaliable Courses\n"
    
    except:
      return "No Courses Are Registred with the Given CRN"

  def sys_add_user(self):
    root.title("Admin Add User Screen")
    AdminSearchCourseFrame = tk.Frame(root, padx=20,pady=20)
    AdminSearchCourseFrame.pack(fill = "both", expand= True)

    def Logout(event=None):
        AdminSearchCourseFrame.pack_forget()
        root.bind('<Return>', enter)
        AdminWindow(self.ID, self.name, self.surname)
    
    def add(event=None):
        name = NameTextBox.get().upper()
        surname = NameTextBox.get().upper()
        title = NameTextBox.get().upper()
        dep = NameTextBox.get().upper()
        email = NameTextBox.get().upper()
        password = NameTextBox.get().upper()
        
        if (len(course) > 0 and len(id) == 5):

            try:
                sql_command = """SELECT CRN_%s FROM STUDENT""" % str(course)
                cursor.execute(sql_command)

            except:
                sql_command = """ALTER TABLE STUDENT ADD COLUMN CRN_%s;""" % str(course)
                cursor.execute(sql_command)
                database.commit()

            sql_command = """UPDATE STUDENT SET CRN_%s="YES" WHERE ID=%d;""" % (str(course), int(id))
            cursor.execute(sql_command)
            database.commit()

        else:
           messagebox.showwarning("Invalid Entry", "No Course or Student was Entered!!")


    IDLabel = Label(AdminSearchCourseFrame, text = "ID:", font='8')
    IDLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER, height=50, width=700)

    IDTextBox = tk.Entry(AdminSearchCourseFrame, font='30')
    IDTextBox.place(relx = 0.5, rely = 0.2, anchor = CENTER, height=50, width=500)
    
    NameLabel = Label(AdminSearchCourseFrame, text = "Name:", font='8')
    NameLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER, height=50, width=700)

    NameTextBox = tk.Entry(AdminSearchCourseFrame, font='30')
    NameTextBox.place(relx = 0.5, rely = 0.2, anchor = CENTER, height=50, width=500)
    
    SurnameLabel = Label(AdminSearchCourseFrame, text = "Surname:", font='8')
    SurnameLabel.place(relx = 0.5, rely = 0.4, anchor = CENTER, height=50, width=800)

    SurnameTextBox = tk.Entry(AdminSearchCourseFrame, font='30')
    SurnameTextBox.place(relx = 0.5, rely = 0.5, anchor = CENTER, height=50, width=500)
    
    TitleLabel = Label(AdminSearchCourseFrame, text = "Title:", font='8')
    TitleLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER, height=50, width=700)

    TitleTextBox = tk.Entry(AdminSearchCourseFrame, font='30')
    TitleTextBox.place(relx = 0.5, rely = 0.2, anchor = CENTER, height=50, width=500)
    
    OfficeLabel = Label(AdminSearchCourseFrame, text = "Office:", font='8')
    OfficeLabel.place(relx = 0.5, rely = 0.4, anchor = CENTER, height=50, width=800)

    OfficeTextBox = tk.Entry(AdminSearchCourseFrame, font='30')
    OfficeTextBox.place(relx = 0.5, rely = 0.5, anchor = CENTER, height=50, width=500)
    
    EmailLabel = Label(AdminSearchCourseFrame, text = "Email:", font='8')
    EmailLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER, height=50, width=700)

    EmailTextBox = tk.Entry(AdminSearchCourseFrame, font='30')
    EmailTextBox.place(relx = 0.5, rely = 0.2, anchor = CENTER, height=50, width=500)
    
    PasswordLabel = Label(AdminSearchCourseFrame, text = "Password:", font='8')
    PasswordLabel.place(relx = 0.5, rely = 0.4, anchor = CENTER, height=50, width=800)

    PasswordTextBox = tk.Entry(AdminSearchCourseFrame, font='30')
    PasswordTextBox.place(relx = 0.5, rely = 0.5, anchor = CENTER, height=50, width=500)
    
    EnterButton = tk.Button(AdminSearchCourseFrame, text = "Enter", height=2, width=15, font='30', command=add)
    EnterButton.place(relx = 0.5, rely = 0.8, anchor = CENTER)
    root.bind('<Return>', add)

    LogoutButton = tk.Button(AdminSearchCourseFrame, text = "Logout", height=2, width=15, font='30', command=Logout)
    LogoutButton.place(relx = 0.5, rely = 0.9, anchor = CENTER)




    
    # ID = Null
    # while (ID == NULL):
    #     try:
    #         ID = int(input("Please enter the ID of the user you would like to add: "))
    #     except:
    #         print("Thats was not a valid input for an ID. Please enter a numerical value.")
    # if ID > 40000 and ID < 30000:
    #     name = input("Enter new user's name: ")
    #     surname = input("Enter new Admin's surname: ")
    #     title = input("Enter new Admin's title: ")
    #     office = input("Enter new Admin's office: ")
    #     email = input("Enter new Admin's email: ")
        
    #     sql_command = """INSERT INTO ADMIN VALUES(""" + ID + """, """ + name + """, """ + surname + """, """ + title + """, """ + office + """, """ + email + """);"""
    #     cursor.execute(sql_command)
    
    # elif ID > 20000:
    #     name = input("Enter new Instructor's name: ")
    #     surname = input("Enter new Instructor's surname: ")
    #     title = input("Enter new Instructor's title: ")
    #     hireYear = input("Enter new Instructor's year of hire: ")
    #     department = input("Enter new Instructor's department: ")
    #     email = input("Enter new Instructor's email: ")

    #     sql_command = """INSERT INTO INSTRUCTOR VALUES(""" + ID + """, """ + name + """, """ + surname + """, """ + title + """, """ + hireYear + """, """ + department + """, """ + email + """);"""
    #     cursor.execute(sql_command) 
    
    # elif ID > 10000:
    #     name = input("Enter new Student's name: ")
    #     surname = input("Enter new Student's surname: ")
    #     gradYear = input("Enter new Student's expected graduation year: ")
    #     major = input("Enter new Student's major: ")
    #     email = input("Enter new Student's email: ")
    #     password = input("Enter new Student's password: ")

    #     sql_command = """INSERT INTO STUDENT VALUES(""" + str(ID) + """, """ + name + """, """ + surname + """, """ + gradYear + """, """ + major + """, """ + email + """, """  + password + """);"""
    #     cursor.execute(sql_command) 
        
    # else:
    #     print("Invalid ID! No User was Removed Due to no User being Selected")
        
    # database.commit()

  def sys_drop_user(self):
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
    
    database.commit()

  def course_add_student(self):
    root.title("Admin Add Student to Course Screen")
    AdminSearchCourseFrame = tk.Frame(root, padx=20,pady=20)
    AdminSearchCourseFrame.pack(fill = "both", expand= True)

    def Logout(event=None):
        AdminSearchCourseFrame.pack_forget()
        root.bind('<Return>', enter)
        AdminWindow(self.ID, self.name, self.surname)
    
    def add(event=None):
        course = CourseTextBox.get().upper()
        id = str(StudentTextBox.get())
        if (len(course) > 0 and len(id) == 5):

            try:
                sql_command = """SELECT CRN_%s FROM STUDENT""" % str(course)
                cursor.execute(sql_command)

            except:
                sql_command = """ALTER TABLE STUDENT ADD COLUMN CRN_%s;""" % str(course)
                cursor.execute(sql_command)
                database.commit()

            sql_command = """UPDATE STUDENT SET CRN_%s="YES" WHERE ID=%d;""" % (str(course), int(id))
            cursor.execute(sql_command)
            database.commit()

        else:
           messagebox.showwarning("Invalid Entry", "No Course or Student was Entered!!")


    CourseLabel = Label(AdminSearchCourseFrame, text = "Please Enter the CRN of a Course You Would Like to Add a Student In:", font='8')
    CourseLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER, height=50, width=700)

    CourseTextBox = tk.Entry(AdminSearchCourseFrame, font='30')
    CourseTextBox.place(relx = 0.5, rely = 0.2, anchor = CENTER, height=50, width=500)
    
    question = "Please Enter the ID of the Student You Would Like to Add to the Course Listed Above:"
    StudentLabel = Label(AdminSearchCourseFrame, text = question, font='8')
    StudentLabel.place(relx = 0.5, rely = 0.4, anchor = CENTER, height=50, width=800)

    StudentTextBox = tk.Entry(AdminSearchCourseFrame, font='30')
    StudentTextBox.place(relx = 0.5, rely = 0.5, anchor = CENTER, height=50, width=500)
    
    EnterButton = tk.Button(AdminSearchCourseFrame, text = "Enter", height=2, width=15, font='30', command=add)
    EnterButton.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    root.bind('<Return>', add)

    LogoutButton = tk.Button(AdminSearchCourseFrame, text = "Logout", height=2, width=15, font='30', command=Logout)
    LogoutButton.place(relx = 0.5, rely = 0.9, anchor = CENTER)

  def course_drop_student(self):
    root.title("Admin Drop Student from Course Screen")
    AdminSearchCourseFrame = tk.Frame(root, padx=20,pady=20)
    AdminSearchCourseFrame.pack(fill = "both", expand= True)

    def Logout(event=None):
        AdminSearchCourseFrame.pack_forget()
        root.bind('<Return>', enter)
        AdminWindow(self.ID, self.name, self.surname)
    
    def add(event=None):
        course = CourseTextBox.get().upper()
        id = str(StudentTextBox.get())
        if (len(course) > 0 and len(id) == 5):

            try:
                sql_command = """SELECT CRN_%s FROM STUDENT""" % str(course)
                cursor.execute(sql_command)

            except:
                sql_command = """ALTER TABLE STUDENT ADD COLUMN CRN_%s;""" % str(course)
                cursor.execute(sql_command)
                database.commit()

            sql_command = """UPDATE STUDENT SET CRN_%s=NULL WHERE ID=%d;""" % (str(course), int(id))
            cursor.execute(sql_command)
            database.commit()

        else:
           messagebox.showwarning("Invalid Entry", "No Course or Student was Entered!!")


    CourseLabel = Label(AdminSearchCourseFrame, text = "Please Enter the CRN of a Course You Would Like to Add a Student In:", font='8')
    CourseLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER, height=50, width=700)

    CourseTextBox = tk.Entry(AdminSearchCourseFrame, font='30')
    CourseTextBox.place(relx = 0.5, rely = 0.2, anchor = CENTER, height=50, width=500)
    
    question = "Please Enter the ID of the Student You Would Like to Add to the Course Listed Above:"
    StudentLabel = Label(AdminSearchCourseFrame, text = question, font='8')
    StudentLabel.place(relx = 0.5, rely = 0.4, anchor = CENTER, height=50, width=800)

    StudentTextBox = tk.Entry(AdminSearchCourseFrame, font='30')
    StudentTextBox.place(relx = 0.5, rely = 0.5, anchor = CENTER, height=50, width=500)
    
    EnterButton = tk.Button(AdminSearchCourseFrame, text = "Enter", height=2, width=15, font='30', command=add)
    EnterButton.place(relx = 0.5, rely = 0.75, anchor = CENTER)
    root.bind('<Return>', add)

    LogoutButton = tk.Button(AdminSearchCourseFrame, text = "Logout", height=2, width=15, font='30', command=Logout)
    LogoutButton.place(relx = 0.5, rely = 0.9, anchor = CENTER)
  
  def course_roster(self):
      course = input("Please enter the course you would like the roster for:").upper()
      print("Here is the roster for course", course, "\n\nROSTER")
      database.commit()



######################################################  DO NOT TOUCH BELOW THIS LINE    #####################################################################################################################################################################################################################

#Student Screen
def StudentWindow(ID, name, surname):
    root.title("Student Screen")
    StudentFrame = tk.Frame(root, padx=20,pady=20)
    StudentFrame.pack(fill = "both", expand= True)
    u = Student(name, surname, ID)

    def Logout(event=None):
        StudentFrame.pack_forget()
        root.bind('<Return>', enter)
        LoginFrame.pack(fill = "both", expand= True)

    def Forget(event=None):
       StudentFrame.pack_forget()

    ChoiceLabel = Label(StudentFrame, text = "Select One of the Options Below", font='20')
    ChoiceLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)

    SearchCourseButton = tk.Button(StudentFrame, text = "Search For a Course", height=2, width=25, font='30', command=sequence(Forget, u.searchcourse))
    SearchCourseButton.place(relx = 0.5, rely = 0.3, anchor = CENTER)

    AddCourseButton = tk.Button(StudentFrame, text = "Add a Course", height=2, width=25, font='30', command=sequence(Forget, u.addcourse))
    AddCourseButton.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    DropCourseButton = tk.Button(StudentFrame, text = "Drop a Course", height=2, width=25, font='30', command=sequence(Forget, u.dropcourse))
    DropCourseButton.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    ScheduleButton = tk.Button(StudentFrame, text = "Look at Schedule", height=2, width=25, font='30', command=sequence(Forget, u.show_schedule))
    ScheduleButton.place(relx = 0.5, rely = 0.7, anchor = CENTER)

    LogoutButton = tk.Button(StudentFrame, text = "Logout", height=2, width=15, font='30', command=Logout)
    LogoutButton.place(relx = 0.5, rely = 0.9, anchor = CENTER)
    root.bind('<Return>', Logout)

#Instructor Screen
def InstructorWindow(ID, name, surname):
    root.title("Instructor Screen")
    InstructorFrame = tk.Frame(root, padx=20,pady=20)
    InstructorFrame.pack(fill = "both", expand= True)
    u = Instructor(name, surname, ID)
    
    def Logout(event=None):
        InstructorFrame.pack_forget()
        root.bind('<Return>', enter)
        LoginFrame.pack(fill = "both", expand= True)

    def Forget(event=None):
       InstructorFrame.pack_forget()

    ChoiceLabel = Label(InstructorFrame, text = "Select One of the Options Below", font='20')
    ChoiceLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)

    SearchCourseButton = tk.Button(InstructorFrame, text = "Search For a Course", height=2, width=25, font='30', command=sequence(Forget, u.searchcourse))
    SearchCourseButton.place(relx = 0.5, rely = 0.3, anchor = CENTER)

    ClassListButton = tk.Button(InstructorFrame, text = "Look at Class List", height=2, width=25, font='30', command=sequence(Forget, u.show_classlist))
    ClassListButton.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    ScheduleButton = tk.Button(InstructorFrame, text = "Look at Schedule", height=2, width=25, font='30', command=sequence(Forget, u.show_schedule))
    ScheduleButton.place(relx = 0.5, rely = 0.7, anchor = CENTER)

    LogoutButton = tk.Button(InstructorFrame, text = "Logout", height=2, width=15, font='30', command=Logout)
    LogoutButton.place(relx = 0.5, rely = 0.9, anchor = CENTER)
    root.bind('<Return>', Logout)

#Admin Screen
def AdminWindow(ID, name, surname):
    root.title("Admin Screen")
    AdminFrame = tk.Frame(root, padx=20,pady=20)
    AdminFrame.pack(fill = "both", expand= True)
    u = Admin(name, surname, ID)
    
    def Logout(event=None):
        AdminFrame.pack_forget()
        root.bind('<Return>', enter)
        LoginFrame.pack(fill = "both", expand= True)

    def Forget(event=None):
       AdminFrame.pack_forget()

    ChoiceLabel = Label(AdminFrame, text = "Select One of the Options Below", font='20')
    ChoiceLabel.place(relx = 0.5, rely = 0.1, anchor = CENTER)

    AddCourseButton = tk.Button(AdminFrame, text = "Add a Course to the System", height=1, width=30, font='30', command=sequence(Forget, u.sys_addCourse))
    AddCourseButton.place(relx = 0.5, rely = 0.2, anchor = CENTER)

    DropCourseButton = tk.Button(AdminFrame, text = "Drop a Course from the System", height=1, width=30, font='30', command=sequence(Forget, u.sys_dropCourse))
    DropCourseButton.place(relx = 0.5, rely = 0.3, anchor = CENTER)

    AddUserButton = tk.Button(AdminFrame, text = "Add a User to the System", height=1, width=30, font='30', command=sequence(Forget, u.sys_add_user))
    AddUserButton.place(relx = 0.5, rely = 0.4, anchor = CENTER)

    DropUserButton = tk.Button(AdminFrame, text = "Drop a User from the System", height=1, width=30, font='30', command=sequence(Forget, u.sys_drop_user))
    DropUserButton.place(relx = 0.5, rely = 0.5, anchor = CENTER)

    AddStudentToCourseButton = tk.Button(AdminFrame, text = "Add a Student to a Course", height=1, width=30, font='30', command=sequence(Forget, u.course_add_student))
    AddStudentToCourseButton.place(relx = 0.5, rely = 0.6, anchor = CENTER)

    DropStudentToCourseButton = tk.Button(AdminFrame, text = "Drop a Student From a Course", height=1, width=30, font='30', command=sequence(Forget, u.course_drop_student))
    DropStudentToCourseButton.place(relx = 0.5, rely = 0.7, anchor = CENTER)

    CourseRosterButton = tk.Button(AdminFrame, text = "Look at a Course Roster", height=1, width=30, font='30', command=sequence(Forget, u.course_roster))
    CourseRosterButton.place(relx = 0.5, rely = 0.8, anchor = CENTER)

    LogoutButton = tk.Button(AdminFrame, text = "Logout", height=2, width=15, font='30', command=Logout)
    LogoutButton.place(relx = 0.5, rely = 0.93, anchor = CENTER)
    root.bind('<Return>', Logout)

#Idenity Verification
def enter(event=None):
    # email = UsernameTextBox.get().upper()////////////////////////////////////////////////////////////////////////////////////////////////////////////////////
    # password = PasswordTextBox.get()
    email = "RUBINV"
    password = "pass32"
    user = "Invalid Login!!!"
    while (user == "Invalid Login!!!"):
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
                    messagebox.showwarning("Invalid Entry", "Not a Valid Credential")
                    break                   
                    
                else:
                    ID = query_result[0][0]
                    name = query_result[0][1]
                    surname = query_result[0][2]
                    UsernameTextBox.delete(0, END)
                    PasswordTextBox.delete(0, END)
                    LoginFrame.pack_forget()
                    AdminWindow(ID, name, surname)
                    break
            else:
                ID = query_result[0][0]
                name = query_result[0][1]
                surname = query_result[0][2]
                UsernameTextBox.delete(0, END)
                PasswordTextBox.delete(0, END)
                LoginFrame.pack_forget()
                InstructorWindow(ID, name, surname)
                break
        else:
            ID = query_result[0][0]
            name = query_result[0][1]
            surname = query_result[0][2]
            UsernameTextBox.delete(0, END)
            PasswordTextBox.delete(0, END)
            LoginFrame.pack_forget()
            StudentWindow(ID, name, surname)
            break
    


#Login Screen
LoginFrame = tk.Frame(root, padx=20,pady=20)
LoginFrame.pack(fill = "both", expand= True)

WelcomeLabel = Label(LoginFrame, text = "Welcome to Leopard Web", font='20')
WelcomeLabel.place(relx = 0.5, rely = 0.11, anchor = CENTER)

LoginLabel = Label(LoginFrame, text = "Please Login Using Your Credentials", font='20')
LoginLabel.place(relx = 0.5, rely = 0.19, anchor = CENTER)

UsernameLabel = Label(LoginFrame, text = "Email:", font='20')
UsernameLabel.place(relx = 0.5, rely = 0.33, anchor = CENTER, height=50, width=500)

UsernameTextBox = tk.Entry(LoginFrame, font='30')
UsernameTextBox.place(relx = 0.5, rely = 0.4, anchor = CENTER, height=50, width=500)

PasswordLabel = Label(LoginFrame, text = "Password:", font='20')
PasswordLabel.place(relx = 0.5, rely = 0.53, anchor = CENTER, height=50, width=500)

PasswordTextBox = tk.Entry(LoginFrame, font='30')
PasswordTextBox.place(relx = 0.5, rely = 0.6, anchor = CENTER, height=50, width=500)

EnterButton = tk.Button(LoginFrame, text = "Enter", height=2, width=15, font='30', command=enter)
EnterButton.place(relx = 0.5, rely = 0.8, anchor = CENTER)
root.bind('<Return>', enter)

mainloop()
database.commit()         
database.close()