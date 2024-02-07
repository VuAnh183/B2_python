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
    self.__course[course_id] = {"Name": course_name, "Mark": ""}
    
  def addMark(self, course_id, mark):
    self.__course[course_id]["Mark"] = mark

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
      
      
  def displayStudentList(self):     
    print("----------------------------------------------------------------")
    print("Student list:")
    count = 1
    for x in self.__std_list:
      print(f"{count}) {self.__std_list[x].getStdName()}")
      count += 1 
            
  def displayCourseList(self):
    print("----------------------------------------------------------------")
    print("Course list:")
    count = 1
    for x in self.__course_list:
      print(f"{count}) {self.__course_list[x].getCourseName()}")
      count += 1  
      

  def listFuncion(self):
    print("LIST OF FUNCTIONS: \n")
    print("1. List courses")
    print("2. List student")
    print("3. Input mark")
    print("4. Print mark ")
    print("5. Exit")
    print("---")
      
    arg = int(input("Enter a function id: "))
    match arg:
      case 1:
        self.displayCourseList()
        print("---")
        return self.listFuncion()
      case 2:
        self.displayStudentList()
        print("---")
        return self.listFuncion()
      case 3:
        self.inputMark()
        print("---")
        return self.listFuncion()
      case 4:
        print_mark(course, student)
        print("---")
        return self.listFuncion()
      case 5:
        print("Exit")
        exit()
      case default:
        print("Invalid ID")
        print("--------------------------------")
        return self.listFuncion()


        
func = Function()

func.add_student()
func.displayStudentList()
func.add_course()
func.displayCourseList()

