
def calculate_avg(physics , chemistry , maths):
    return ((physics + chemistry + maths) / 3)

def calculate_percentage(physics , chemistry ,maths):
    total_marks = physics + chemistry + maths
    return (total_marks / 300) * 100

def main():
    student_name = input("Enter the student's name:")
    physics = float(input("Enter the marks for Physics :"))
    chemistry = float(input("Enter the mark of Chemistry :"))
    maths = float(input("Enter the mark of maths :"))
    average = calculate_avg(physics , chemistry  , maths)
    percentage = calculate_percentage(physics , chemistry , maths)
    print(f'Name of the student : {student_name}')
    print(f'Average mark of {student_name} is : {average}')
    print(f'Percentage of {student_name} is : {percentage}%')

if __name__ == "__main__":
    main()    
