import unittest
import sqlite3
from LeopardWeb import Login, menu, Admin

database = sqlite3.connect("Database.db")
cursor = database.cursor()

class Test(unittest.TestCase):

    def test_Login(self):
        passfail = []

        if (self.assertEqual(Login("telsan", "pass3"), "Student")):
            passfail.append(True)
        else:
            passfail.append(False)
        if (self.assertEqual(Login("galileig", "pass22"), "Instructor")):
            passfail.append(True)
        else:
            passfail.append(False)
        if (self.assertEqual(Login("rubinv", "pass32"), "Admin")):
            passfail.append(True)
        else:
            passfail.append(False)
        if (self.assertEqual(Login("smth", "wrong456"), "Invalid Login!!\n")):
            passfail.append(True)
        else:
            passfail.append(False)
            
        return passfail

    def test_Logout(self):
        self.assertEqual(menu("Student", "isaac", "newton", 10001, "4"), "Logging Off")
        self.assertEqual(menu("Instructor", "Nelson", "Patrick", 20002, "5"), "Logging Off")
        self.assertEqual(menu("Admin", "Vera", "rubin", 30002,"6"), "Logging Off")

    
    def test_sys_addCourse(self):
        a = Admin("First", "Last", 00000)
        self.assertEqual(a.sys_addCourse(10, "title", "department", "day", "semester", 7890, 1, "time", "Random Teach"), "Course Added to Course Table. Course Column Added to Student Table.")


    def testsys_dropCourse(self):
        a = Admin("First", "Last", 00000)
        self.assertEqual(a.sys_dropCourse(10), "CRN_10 was Deleted From the List of Avaliable Courses\n")
        self.assertEqual(a.sys_dropCourse(2344), "No Courses Are Registred with the Given CRN")



    #  def test_Displayer_Menu(self):
    #         self.assertEqual(display_menu("Student"), "\n 1)Search Courses \n 2)Add/Drop Course \n 3)Print Schedule \n 4)Logout \n")
    #         self.assertEqual(display_menu("Instructor"), "\n 1)Print Schedule \n 2)Print Classlist \n 3)Search for Courses \n 4)Assign one course to each instructor and search based on course \n 5)Logout \n")
    #         self.assertEqual(display_menu("Admin"), "\n 1)Add course to System \n 2)Remove course from system \n 3)Add/Remove user \n 4)Add/Remove student from course  \n 5)Search and Print Course Roster \n 6)Logout \n")

    # def test_Menu(self):
    #     self.assertEqual(menu("Student", "1"), "Student")
    #     self.assertEqual(menu("Student", "2"), "Student")
    #     self.assertEqual(menu("Student", "3"), "Student")
    #     self.assertEqual(menu("Student", "4"), "Student")
    #     self.assertEqual(menu("Student", "5"), "Student")

    #     self.assertEqual(menu("Instructor", "1"), "Student")
    #     self.assertEqual(menu("Instructor", "2"), "Student")
    #     self.assertEqual(menu("Instructor", "3"), "Student")
    #     self.assertEqual(menu("Instructor", "4"), "Student")
    #     self.assertEqual(menu("Instructor", "5"), "Student")
    #     self.assertEqual(menu("Instructor", "6"), "Student")

    #     self.assertEqual(menu("Admin", "1"), "Student")
    #     self.assertEqual(menu("Admin", "2"), "Student")
    #     self.assertEqual(menu("Admin", "3"), "Student")
    #     self.assertEqual(menu("Admin", "4"), "Student")
    #     self.assertEqual(menu("Admin", "5"), "Student")
    #     self.assertEqual(menu("Admin", "6"), "Student")
    #     self.assertEqual(menu("Admin", "7"), "Student")