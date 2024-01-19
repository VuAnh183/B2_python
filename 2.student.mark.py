class Student:
    
  def numStd():
    numStd = int(input("Enter the number of students: "))
    
  def setAttr(self):
    for i in Student.numStd():
      self.__std_name = str(input("Enter student name: "))
      self.__std_age = int(input("Enter student age: "))
    
  def getStdName(self):
    return self.__std_name
    
  def getStdAge(self):
    return self.__std_age
  
  
  def describe(self):
    for i in Student.numStd:
      print(f"Name: {self.std_name}")
      print(f"Age: {self.std_age}")

class Course:
  
  def __init__(self):
    self.course_name = str(input("Enter course name: "))
    
  def describe(self):
    print(f"Course name: {self.course_name}")
    
class StudentMark:
  
  def __init__(self):
    for i in Course.course_name:
      self.mark_name = Course.course_name[i]
      self.mark = int(input(f"Enter mark for {self.mark_name}: "))
      
  def describe(self):
    print(f"Mark for {self.mark_name}: {self.mark}")
  
def main():
  student = Student()
  student.describe()

  course = Course()
  course.describe()
  
  
main()