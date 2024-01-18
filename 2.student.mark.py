class Student:
  
  def __init__(self):
    self.name = str(input("Enter student name: "))
    self.age = int(input("Enter student age: "))
    
  def describe(self):
    print(f"Name: {self.name}")
    print(f"Age: {self.age}")

class Course:
  def __init__(self):
    self.name = str(input("Enter course name: "))
    
  def describe(self):
    print(f"Course name: {self.name}")
    
  
  
def main():
  student = Student()
  student.describe()

  course = Course()
  course.describe()
  
  
main()