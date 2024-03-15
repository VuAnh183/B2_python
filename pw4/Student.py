import math

class Student:
  # Constructor 
  def __init__(self, id, name, DoB):
    self.__id = id
    self.__name = name
    self.__DoB = DoB
    self.__marks = {}
    self.__gpa = 0
    
  def getStdId(self):
    return self.__id
  
  def getStdName(self):
    return self.__name
  
  def getStdDoB(self):
    return self.__DoB
  
  def getStdMark(self):
    return self.__marks
  
  def getGPA(self):
    sum = 0
    if len(self.__marks) == 0:
      return self.__gpa
    else:
      for x, y in self.__marks.items():
        sum += y
        
      #Round down the GPA to 1-digit decimal number
      self.__gpa = math.floor((sum / len(self.__marks)) * 10) / 10
      return self.__gpa
    
  def getMark(self, course_name):
    return self.__marks.get(course_name)
    
  def input_mark(self, course_name, mark):
    self.__marks[course_name] = mark
    
  
  def __str__(self):
    return f"Student ID: {self.__id}, Student Name: {self.__name}, Date of Birth: {self.__DoB}"