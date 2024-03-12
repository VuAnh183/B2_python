class Student:
  # Constructor 
  def __init__(self, id, name, DoB):
    self.__id = id
    self.__name = name
    self.__DoB = DoB
    self.__course = {}
    
    
  def getStdId(self):
    return self.__id
  
  def getStdDoB(self):
    return self.__DoB
  
  def getStdName(self):
    return self.__name
  
  def getAge(self):
    return self.__age
  
  def getCourse(self):
    return self.__course
  
  def addCourse(self, course_id, course_name):
    # if course_name in self.__course.values() == True:
      self.__course[course_id] = {"Name": course_name, "Mark": ""}
      course_values = self.__course.values()
      print(course_values)
    # else: 
      # print("Course already exists!")
    
  def addMark(self, course_id, mark):
    self.__course[course_id]["Mark"] = mark
    
  def getMark(self, course_id):
    return self.__course[course_id]["Mark"]

class Course:
  def __init__(self, id, name):
    self.__course_id = id
    self.__course_name = name
  
  def getCourseId(self):
    return self.__course_id
  
  def getCourseName(self): 
    return self.__course_name
  

    
class Function(Student, Course):
  
  def __init__(self):
    self.__std_list = {}
    self.__course_list = {}
  
  def getStudentList(self):
    return self.__std_list
  
  def getCourseList(self):
    return self.__course_list
  
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
      self.__std_list[std_id] = Student(std_id, std_name, std_DOB)
      
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
      self.__course_list[course_id] = Course(course_id, course_name)
      for y in self.__std_list:
        self.__std_list[y].addCourse(course_id, course_name)
      
      
  def inputMark(self):
    print("----------------------------------------------------------------")
    c_id = int(input("Enter course ID: "))
    for x in self.__std_list:
      print("Enter", self.__std_list[x].getStdName(), "mark: ")
      mark = input()
      self.__std_list[x].addMark(c_id, mark)
      
  
  # Display students marks 
  def printMark(self):
    print("----------------------------------------------------------------")
    c_id = int(input("Enter course ID: "))
    
    # Get course name from list
    print(f"{self.__course_list[c_id].getCourseName()} marks: ")
    
    # Get students name and mark
    for x in self.__std_list:
      print(f"{self.__std_list[x].getStdName()}: {self.__std_list[x].getMark(c_id)}")
      
  # Display student list
  def displayStudentList(self):     
    print("----------------------------------------------------------------")
    print("Student list:")
    
    # Check if there are any student in the list 
    if len(self.__std_list) == 0:
      print("There are no student record")
      print("Please add students before trying this function again!") 
      
    # Display students names
    count = 1
    for x in self.__std_list:
      print(f"{count}) {self.__std_list[x].getStdName()}")
      count += 1 
  
  # Display course list 
  def displayCourseList(self):
    print("----------------------------------------------------------------")
    print("Course list:")
    
    # Check if there are any course in the list 
    if len(self.__course_list) == 0:
      print("There are no course record")
      print("Please add courses before trying this function again!") 
    
    # Display courses names
    count = 1
    for x in self.__course_list:
      print(f"{count}) {self.__course_list[x].getCourseName()}")
      count += 1  
      

  # List of functions
  def listFuncion(self):
    print("LIST OF FUNCTIONS: \n")
    print("1. Add students")
    print("2. Add courses")
    print("3. List students")
    print("4. List courses")
    print("5. Input mark")
    print("6. Print mark ")
    print("7. Exit")
    print("---")
      
    arg = int(input("Choose a function: "))
    match arg:
      case 1: 
        self.add_student()
        print("\n\n\n")
        print("---")
        return self.listFuncion()
      case 2:
        self.add_course()
        print("\n\n\n")
        print("---")
        return self.listFuncion()
      case 3:
        self.displayStudentList()
        print("\n\n\n")
        print("---")
        return self.listFuncion()
      case 4:
        self.displayCourseList()
        print("\n\n\n")
        print("---")
        return self.listFuncion()
      case 5:
        self.inputMark()
        print("\n\n\n")
        print("---")
        return self.listFuncion()
      case 6:
        self.printMark()
        print("\n\n\n")
        print("---")
        return self.listFuncion()
      case 7:
        print("Exit")
        exit()
      case default:
        print("Invalid")
        print("--------------------------------")
        print("\n\n\n")
        print("---")
        return self.listFuncion()
        
func = Function()

func.listFuncion()

