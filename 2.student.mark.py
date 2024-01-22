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
  
  def getCourseId(self):
    return self.__course_id
  
  def getCourseName(self): 
    return self.__course_name
  
  def display(self):
    print("--------------------------------")
    print("ID:", self.__course_id)
    print("Name:", self.__course_name)

  
  def addMark():
    id = int(input("Enter course ID:"))
    mark = float(input("Enter student mark: "))
 
 
                
def func(Student, Course):
  student = {}
  course = {}
  print("--------------------------------------------------------")
  numStd = int(input("Enter number of students: "))
  
  # def getStdInfo():
  for x in range(numStd):
    print(f"Student number {x+1}")
    student[x] = Student()
  
  # def displayStd():
  for y in range(numStd):
    print(f"Student number {y+1}")
    student[y].display()  
  
  print("--------------------------------------------------------")
  numCourse = int(input("Enter number of courses: "))
  
  for x in range(numCourse):
    print(f"Course number {x+1}")
    course[x] = Course()
    
  print("--------------------------------------------------------")  
  for y in range(numCourse):
    print(f"Course number {y+1}")
    course[y].display()
  
  
  print("--------------------------------------------------------")  
  print("Input Marks:")
  id = int(input("Enter the course ID: "))
  for x in range(numCourse):
    if id == course[x].getCourseId():
      name = course[x].getCourseName()
      for y in range(numStd):
        mark = float(input(f"Student {student[y].getStdName()}'s mark: "))
        setattr(student[y], "mark", mark)
        
        
  print("--------------------------------------------------------")
  print("List Marks:")
  id = int(input("Enter the course ID: "))
  name = course[x].getCourseName()
  print(f"{name} mark:")
  for x in range(numCourse):
    if id == course[x].getCourseId():
      for y in range(numStd):
        print(f"{student[y].getStdName()}:", student[y].mark)
     
  
func(Student, Course)