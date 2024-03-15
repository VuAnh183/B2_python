class Course:
  def __init__(self, id, name):
    self.__course_id = id
    self.__course_name = name
  
  def getCourseId(self):
    return self.__course_id
  
  def getCourseName(self): 
    return self.__course_name
  
  def __str__(self):
    return f"Course ID: {self.__course_id}, Course Name: {self.__course_name}"