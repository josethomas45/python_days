
def greet(first_name, last_name):
    return f"Hello, {first_name} {last_name}! \n"


message = greet("jikku", "thomas")
text = greet("jose", "thomas")
message1 = greet("awin das", "r")

with open("jikku.txt", "w") as file:
    file.write(message)
    file.write(text)
    file.write(message1)
    
