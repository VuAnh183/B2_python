import math 
import numpy as np
from pw4.Student import Student
from pw4.Course import Course

class Function:
  
  def __init__(self):
    self.__std_list = []
    self.__course_list = []
    
  
  def add_student(self):
    print("----------------------------------------------------------------")
    std_num = int(input("Enter number of students: "))
    
    for x in range(std_num):
      print("----------------------")
      print(f"Student number {x+1}")
      try:
        std_id = int(input("Enter student ID: "))
        std_name = input("Enter student name: ")
        std_DOB = input("Enter DOB: ")
      except:
        print("Invalid input!")
        exit()
        
        
      self.__std_list.append(Student(std_id, std_name, std_DOB))
      
  def add_course(self):
    print("----------------------------------------------------------------")
    course_num = int(input("Enter number of courses: "))
    
    for x in range(course_num):
      print("----------------------")
      print(f"Course number {x+1}")
      try:
        course_id = int(input("Enter course ID: "))
        course_name = input("Enter course name: ")
      except:
        print("Invalid input!")
        exit()
        
        
      self.__course_list.append(Course(course_id, course_name))
      
  #Input Student's mark    
  def inputMark(self):
    print("----------------------------------------------------------------")
    try:
      c_name = input("Enter course name: ")
    except:
      print("Invalid input!")
      exit()
      
    if len(self.__std_list) == 0:
      print("Please add students before trying this function again!")
    else:
      for student in self.__std_list:
        mark = float(input(f"Enter {student.getStdName()}'s mark: "))
        
        #Round down the mark to 1-digit decimal number
        mark = math.floor(mark * 10) / 10
        student.input_mark(c_name, mark)
    
  # Display students marks 
  def printMark(self):
    print("----------------------------------------------------------------")
    
    try:
      c_name = input("Enter course name: ")
    except:
      print("Invalid input!")
      exit()
    
    print(f"\nMarks for {c_name}:")
      
    # Get students name and mark
    for student in self.__std_list:
      if c_name in student.getStdMark():
        print(f"{student.getStdName()}: {student.getMark(c_name)}")
      else:
        print(f"{student.getStdName()}: Unavailable")
      
  # Display student list
  def displayStudentList(self):     
    print("----------------------------------------------------------------")
    print("Student list:")
    
    # Check if there are any student in the list 
    if len(self.__std_list) == 0:
      print("There are no student record")
      print("Please add students before trying this function again!") 
      
    # Display students names
    for student in self.__std_list:
      print(student)
  
  # Display course list 
  def displayCourseList(self):
    print("----------------------------------------------------------------")
    print("Course list:")
    
    # Check if there are any course in the list 
    if len(self.__course_list) == 0:
      print("There are no course record")
      print("Please add courses before trying this function again!") 
    
    # Display courses names
    for course in self.__course_list:
      print(course)
      

  def calGPA(self):
    print("----------------------------------------------------------------")
    if len(self.__std_list) == 0:
        print("Please add students before trying this function again!")
    else:
        #Create a list to store student's name and GPA
        gpa = [(student.getStdName(), student.getGPA()) for student in self.__std_list]
        
        #Convert it to numpy array
        gpa_array = np.array(gpa)
        
        # Sort the array in ascending order
        sorted_indices = np.argsort(gpa_array[:, 1])[::-1] 
        # Reverse the array for descending order
        sorted_gpas = gpa_array[sorted_indices]
      
        print("Students sorted by GPA in descending order:")
        for name, gpa in sorted_gpas:
            print(f"{name}: {gpa}")
  # List of functions
  def listFuncion(self):
    print("LIST OF FUNCTIONS: \n")
    print("1. Add students")
    print("2. Add courses")
    print("3. List students")
    print("4. List courses")
    print("5. Input mark")
    print("6. Print mark ")
    print("7. Show GPA")
    print("8. Exit")
    print("---")
      
    arg = int(input("Choose a function: "))
    match arg:
      case 1: 
        self.add_student()
        print("\n\n")
        print("---")
        return self.listFuncion()
      case 2:
        self.add_course()
        print("\n\n")
        print("---")
        return self.listFuncion()
      case 3:
        self.displayStudentList()
        print("\n\n")
        print("---")
        return self.listFuncion()
      case 4:
        self.displayCourseList()
        print("\n\n")
        print("---")
        return self.listFuncion()
      case 5:
        self.inputMark()
        print("\n\n")
        print("---")
        return self.listFuncion()
      case 6:
        self.printMark()
        print("\n\n")
        print("---")
        return self.listFuncion()
      case 7: 
        self.calGPA()
        print("\n\n")
        print("---")
        return self.listFuncion()
      case 8:
        print("Exit")
        exit()
      case default:
        print("Invalid")
        print("--------------------------------")
        print("\n\n")
        print("---")
        return self.listFuncion()
        


