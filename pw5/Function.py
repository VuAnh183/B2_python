import math 
import os
import numpy as np
from Student import Student
from Course import Course


class Function:
  
  def __init__(self):
    self.__std_list = []
    self.__course_list = []
    
  
  def add_student(self):
    print("----------------------------------------------------------------")
    
    std_num = int(input("Enter number of students: "))
    
    # Create a text file for students
    std_file = "students.txt"
    
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
      
      #Write student info to file
      with open(std_file, 'a') as file:
        file.write(f"Student ID: {std_id}, Student Name: {std_name}, Date of Birth: {std_DOB} \n")
        
  def add_course(self):
    print("----------------------------------------------------------------")
    course_num = int(input("Enter number of courses: "))
    
    # Create a text file for courses
    course_file = "courses.txt"
    
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
      
      # Write course info to file
      with open("courses.txt", 'a') as file:
        file.write(f"Course ID: {course_id}, Course Name: {course_name} \n")
        
  #Input Student's mark    
  def inputMark(self):
    print("----------------------------------------------------------------")
    try:
      c_name = input("Enter course name: ")
    except:
      print("Invalid input!")
      exit()
    
    # Create text file for marks   
    marks_file = "marks.txt"
    
    if len(self.__std_list) == 0:
      print("Please add students before trying this function again!")
    else:
      for student in self.__std_list:
        mark = float(input(f"Enter {student.getStdName()}'s mark: "))
        
        #Round down the mark to 1-digit decimal number
        mark = math.floor(mark * 10) / 10
        student.input_mark(c_name, mark)
        
        # Write mark to file
        with open("marks.txt", "a") as file:
          file.write(f"Student: {student.getStdName()}, Course: {c_name}, Mark: {mark} \n")
    
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
      
        # Unsort the array to get the correct order
        unsorted_indices = np.argsort(sorted_indices)
        final_sorted_gpas = sorted_gpas[unsorted_indices]
      
        print("Students sorted by GPA in descending order:")
        for name, gpa in final_sorted_gpas:
            print(f"{name}: {gpa}")
            
  # Delete all text files
  def FileDelete(self):
    os.remove("students.txt")
    os.remove("courses.txt")
    os.remove("marks.txt")
    
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
        self.FileDelete()
        print("Exit")
        exit()
      case default:
        print("Invalid")
        print("--------------------------------")
        print("\n\n")
        print("---")
        return self.listFuncion()
        


