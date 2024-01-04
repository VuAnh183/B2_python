def student_number():
  return int(input("Input the student number: "))

def course_number():
  return int(input("Input numbers of course: "))

def student_info(student, course):
  std_id = int(input("Input the student ID: "))
  std_name = input("Input the student name: ")
  std_DoB = input("Input date of birth: ")
  student[std_id] = {"Name": std_name, "Date of Birth": std_DoB}
  for x in course:
    student[std_id].update({course[x]["Course name"]: ""})
  print("---")
  

def course_info(course):
  course_id = int(input("Input course ID: "))
  course_name = input("Input course name: ")
  course[course_id] = {"Course name": course_name}
  print("---")

  
def list_students(student):
  print("List of students: \n")
  for x, y in student.items(): 
    print(f"{x}: {y}")
  # for x, y in student.items(): 
  #   print(f"{x}: {y}")
  print("--------------------------------------------------------")


def list_courses(course):
  print("List of courses: \n")
  for x, y in course.items():
    print(f"{x}: {y}")
  print("--------------------------------------------------------")
    
    
def input_mark(course, student):
  print("Input course mark: \n")
  course_id = int(input("Enter course id: \n"))
  while 1:
    if course_id in course:
      for x in student:
        print("Enter", student[x]["Name"], "mark: ")
        mark = input()
        student[x].update({course[course_id]["Course name"]: mark})
      print("--------------------------------------------------------")
      break
    else:
      print("Invalid id!!!")
      return input_mark(course, student)
  
      
      
def print_mark(course, student):
  print("Show course mark: \n")
  course_id = int(input("Enter course id: \n"))
  
  while 1:
    if course_id in course:
      for x in student:
        print(student[x]["Name"], student[x][course[course_id]["Course name"]])
      print("--------------------------------------------------------")
      break
    else:
      print("Invalid id!!!")
      return print_mark(course, student)
  
  
    
  
def main():
  student = {}
  course = {}
  course_num = course_number()  
  
  for x in range(course_num):
    print(f"Course {x+1}: \n")
    course_info(course)
     
  list_courses(course)
  
  student_num = student_number()
  
  for x in range(student_num):
    print(f"Student {x+1}: \n")
    x = student
    student_info(student, course)
    
    
  list = list_students(student)

  
  input_mark(course, student)
  
  print_mark(course, student)
  
    
  
main()