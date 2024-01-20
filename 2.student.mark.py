class Student:
  def __init__(self):
    print("--------------------------------")
    self.__std_id = int(input("Enter student ID: "))
    self.__std_name = input("Enter student name: ")
    self.__std_age = int(input("Enter student age: "))
    self.__std_DoB = int(input("Enter student DoB: "))
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
    print("Age:", self.__std_DoB)
    
class Course(Student):
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
  
  def addMark(numStd, mark):
    id = int(input("Enter course ID:"))
    for i in range(numStd):
      mark = float(input(f"Enter {Student[i].getStdName()}'s mark:"))
def main():
  student = {}
  numStd = int(input("Enter number of students: "))
  for x in range(numStd):
    print(f"Student number {x+1}")
    student[x] = Student()
  
  for y in range(numStd):
    print(f"Student number {y+1}")
    student[y].display()  
    
  # for z in range(numStd):
  #   mark = float(input(f"Enter {student[z].getStdName()}'s mark: "))
     
  
main()