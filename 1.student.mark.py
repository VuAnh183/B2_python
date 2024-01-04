def student_number():
  return int(input("Input the student number: "))

def student_info():
  student = {}
  student['id'] = input("Input the student ID: ")
  student['name'] = input("Input the student name: ")
  student['DoB'] = input("Input date of birth: ")
  
def course_number():
  return int(input("Input numbers of course: "))

def main():
  student_num = student_number();
  print(f"Student number: {student_num}")
  
  course_num = course_number()
  print(f"Number of course: {course_num}")
  # student_num = student_info();
  # print(f "Student")
  
main()