age = int(input("Whats your age?"))
student = input("Are you a student? (yes/no)").strip().lower()=="yes"
can_get_discount = (age < 25 and student)
print("you can get a discount " if can_get_discount else "you can't a discount.")


