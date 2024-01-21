class Student:
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
    print("--------------------------------")
    print("Student Info: ")
    print("ID:", self.__std_id)
    print("Name:", self.__std_name)
    print("Age:", self.__std_age)
    print("DoB:", self.__std_DoB)
    
class Course:
  def __init__(self):
    print("--------------------------------")
    self.__course_id = int(input("Enter course ID: "))
    self.__course_name = input("Enter course name: ")
    print("--------------------------------")
  
  def getCourseId(self):
    return self.__course_id
  
  def getCourseName(self): 
    return self.__course_name
  
  def display(self):
    print("--------------------------------")
    print("ID:", self.__course_id)
    print("Name:", self.__course_name)
    print("--------------------------------")
  
  def addMark():
    id = int(input("Enter course ID:"))
    mark = float(input("Enter student mark: "))
                
class func(Student, Course):
  student = {}
  numStd = int(input("Enter number of students: "))
  
  def getStdInfo():
    for x in range(numStd):
      print(f"Student number {x+1}")
      student[x] = Student()
  
  def displayStd():
    for y in range(numStd):
      print(f"Student number {y+1}")
      student[y].display()  
  
  def addMark():
    for i in range(numStd):
      student[i].getStdName() 
      mark = float(input(f"Student {student[i].getStdName()}'s mark: "))
      setattr(student[i], "mark", mark)
      print("Mark:", student[i].mark)
        
     
  
func(Student, Course)