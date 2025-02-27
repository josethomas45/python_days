class Person:
    def __init__(self, fname, lname, dob):
        self.firstname = fname
        self.lastname = lname
        self.date_of_birth = dob  # Added date of birth

    def get_full_name(self):
        return f"{self.firstname} {self.lastname}"

    def get_age(self, current_year):
        birth_year = int(self.date_of_birth.split('/')[-1])
        return current_year - birth_year
    
    def display_info(self):
      print(f"Name: {self.get_full_name()}")
      print(f"Date of Birth: {self.date_of_birth}")


class Student(Person):
    def __init__(self, fname, lname, dob, student_id, grade, courses=None):
        super().__init__(fname, lname, dob)  # Using super()
        self.student_id = student_id
        self.grade = grade
        self.courses = courses if courses is not None else []  # Initialize with an empty list if None

    def add_course(self, course):
        self.courses.append(course)

    def drop_course(self, course):
        if course in self.courses:
            self.courses.remove(course)
        else:
            print(f"Course {course} not found in student's courses.")

    def display_student_info(self, current_year):
        self.display_info()
        print(f"Student ID: {self.student_id}")
        print(f"Grade: {self.grade}")
        print(f"Age: {self.get_age(current_year)}")
        if self.courses:
          print("Courses:")
          for course in self.courses:
              print(f"  - {course}")
        else:
            print("No courses enrolled.")
        
class Teacher(Person):
    def __init__(self, fname, lname, dob, teacher_id, subject):
        super().__init__(fname, lname, dob)
        self.teacher_id = teacher_id
        self.subject = subject
    
    def display_teacher_info(self, current_year):
      self.display_info()
      print(f"Teacher ID: {self.teacher_id}")
      print(f"Subject: {self.subject}")
      print(f"Age: {self.get_age(current_year)}")

def get_student_info():
    print("\n=== Enter Student Information ===")
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    dob = input("Enter date of birth (MM/DD/YYYY): ")
    student_id = input("Enter student ID: ")
    grade = input("Enter grade: ")
    
    student = Student(fname, lname, dob, student_id, grade)
    
    while True:
        course = input("\nEnter course name (or 'done' to finish): ")
        if course.lower() == 'done':
            break
        student.add_course(course)
    
    return student

def get_teacher_info():
    print("\n=== Enter Teacher Information ===")
    fname = input("Enter first name: ")
    lname = input("Enter last name: ")
    dob = input("Enter date of birth (MM/DD/YYYY): ")
    teacher_id = input("Enter teacher ID: ")
    subject = input("Enter subject: ")
    
    return Teacher(fname, lname, dob, teacher_id, subject)

def display_all_records(students, teachers, current_year):
    print("\n=== All School Records ===")
    
    if students:
        print("\nStudent Records:")
        print("-" * 50)
        for i, student in enumerate(students, 1):
            print(f"\nStudent #{i}")
            student.display_student_info(current_year)
    else:
        print("\nNo student records found.")
    
    if teachers:
        print("\nTeacher Records:")
        print("-" * 50)
        for i, teacher in enumerate(teachers, 1):
            print(f"\nTeacher #{i}")
            teacher.display_teacher_info(current_year)
    else:
        print("\nNo teacher records found.")

def main():
    current_year = 2024
    students = []
    teachers = []
    
    while True:
        print("\n=== School Management System ===")
        print("1. Add Student")
        print("2. Add Teacher")
        print("3. Display All Records")
        print("4. Exit")
        
        choice = input("\nEnter your choice (1-4): ")
        
        if choice == '1':
            student = get_student_info()
            students.append(student)
            print("\nStudent Information:")
            student.display_student_info(current_year)
        
        elif choice == '2':
            teacher = get_teacher_info()
            teachers.append(teacher)
            print("\nTeacher Information:")
            teacher.display_teacher_info(current_year)
        
        elif choice == '3':
            display_all_records(students, teachers, current_year)
        
        elif choice == '4':
            display_all_records(students, teachers, current_year)
            print("\nThank you for using the School Management System!")
            break
        
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()