def get_marks(subjects, marks=[]):
    if len(subjects) == 0:
        return marks
    else:
        subject = subjects[0]
        try:
            mark = float(input(f"Enter the mark for {subject}: "))
            if mark < 0 or mark > 100:
                print("Please enter a valid mark between 0 and 100.")
                return get_marks(subjects, marks)
            marks.append(mark)
            return get_marks(subjects[1:], marks)
        except ValueError:
            print("Invalid input. Please enter a number.")
            return get_marks(subjects, marks)

def calculate_average(marks):
    return sum(marks) / len(marks)

def calculate_percentage(marks):
    total_marks = sum(marks)
    return (total_marks / (len(marks) * 100)) * 100

def main():
    student_name = input("Enter the student's name: ")
    subjects = ["Math", "Science", "English"]
    marks = get_marks(subjects)
    average = calculate_average(marks)
    percentage = calculate_percentage(marks)
    print(f"Student Name: {student_name}")
    print(f"Average Marks: {average}")
    print(f"Percentage: {percentage}%")

if __name__ == "__main__":
    main()