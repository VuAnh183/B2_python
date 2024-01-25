class Student:
  # Constructor 
  def __init__(self):
    print("--------------------------------")
    self.__std_id = int(input("Enter student ID: "))
    self.__std_name = input("Enter student name: ")
    self.__std_age = int(input("Enter student age: "))
    self.__std_DoB = input("Enter student DoB: ")
    print("--------------------------------")
    
  def getStdId(self):
    return self.__std_id
  
  def getStdDoB(self):
    return self.__std_DoB
  
  def getStdName(self):
    return self.__std_name
  
  def getAge(self):
    return self.__std_age
  
  
  def display(self):
    print("Student Info: ")
    print("ID:", self.__std_id)
    print("Name:", self.__std_name)
    print("Age:", self.__std_age)
    print("DoB:", self.__std_DoB)
    
  def __setattr__(self, name, mark):
    self.setattr(self, name, mark)
    
class Course:
  def __init__(self):
    print("--------------------------------")
    self.__course_id = int(input("Enter course ID: "))
    self.__course_name = input("Enter course name: ")
  
  def getCourseId(self):
    return self.__course_id
  
  def getCourseName(self): 
    return self.__course_name
  
  def display(self):
    print("ID:", self.__course_id)
    print("Name:", self.__course_name)

    
class Function(Student, Course):
  
  def __init__(self):
    self.__std_num = int(input("Enter number of students: "))
    self.__course_num = int(input("Enter number of courses: "))
    self.__std_list = {}
    self.__course_list = {}
  
  def getStudentList(self):
    return self.__std_list
  
  def getCourseList(self):
    return self.__course_list
  
  def getStdInfo(self):
    for x in range(self.__std_num):
      print(f"Student number {x+1}")
      self.__std_list[x] = Student()
    
  def displayStudentList(self):
    print("----------------------------------------------------------------")
    for x in range(self.__std_num):
      print("--------------------------------")
      print(f"Student number {x+1}")
      self.__std_list[x].display()  
      
  def getCourseInfo(self):
    for x in range(self.__course_num):
      print(f"Course number {x+1}")
      self.__course_list[x] = Course()
      
      
  def displayCourseList(self):
    print("----------------------------------------------------------------")
    for x in range(self.__std_num):
      print("--------------------------------")
      print(f"Course number {x+1}")
      self.__course_list[x].display()  
      

  def inputMark(self):
    print("----------------------------------------------------------------")
    c_id = int(input("Enter course ID: "))
    for x in range(self.__course_num):
      if c_id == self.__course_list[x].getCourseId():
        name = self.__course_list[x].getCourseName()

        
    for x in range(self.__std_num):
      mark = float(input(f"{self.__std_list[x].getStdName()}'s mark: "))
      self.__std_list[x].addMark(name, mark)
      
  # def addMark(self):
  #   id = int(input("Enter course ID: "))
  #   for x in range(self.__std_num):
  #     mark = float(input(f"{self.__std_list[x].getStdName()}'s mark: "))
  #     self.__std_list[x].addMark(self.__course_list[id].getCourseName(), mark)
    

  def getStdNum(self):
    return self.__std_num
  
  def getCourseNum(self):
    return self.__course_num

func = Function()

func.getStdInfo()
func.displayStudentList()

func.getCourseInfo()
func.displayCourseList()

func.inputMark()