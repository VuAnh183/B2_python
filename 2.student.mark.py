class Student(Course):
  # Constructor 
  def __init__(self):
    print("--------------------------------")
    self.__id = int(input("Enter student ID: "))
    self.__name = input("Enter student name: ")
    self.__age = int(input("Enter student age: "))
    self.__DoB = input("Enter student DoB: ")
    
  def getStdId(self):
    return self.__id
  
  def getStdDoB(self):
    return self.__DoB
  
  def getStdName(self):
    return self.__name
  
  def getAge(self):
    return self.__age
  
  
  def display(self):
    print("Student Info: ")
    print("ID:", self.__id)
    print("Name:", self.__name)
    print("Age:", self.__age)
    print("DoB:", self.__DoB)
    
    
    
  def addMark(self, name, mark):
    setattr(self, name, mark)
    print("Score updated!")
    print(vars(self))
    
  def getMark(self, name):
    return self.name
  
  

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
      
  def printMark(self):
    name = input("Enter course name: ")
    for x in range(self.__std_num):
      print(f"{self.__std_list[x].getStdName()}'s mark: {self.__std_list[x].getMark(name)}")
      print("--------------------------------------------------------")
  def getStdNum(self):
    return self.__std_num
  
  def getCourseNum(self):
    return self.__course_num

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

func.getStdInfo()
func.displayStudentList()

func.getCourseInfo()
func.displayCourseList()

func.inputMark()
func.printMark()