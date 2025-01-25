ent_string = input("enter the string you like to check : ")

#1

uppercase_strng = ent_string.upper()
lowercase_strng = ent_string.lower()

print(f"Orginal string : {ent_string}")
print(f"Uppercase string : {uppercase_strng}")
print(f"Lowercase string :{lowercase_strng}")

#2

length_of_strng = len(ent_string)

print(f"Length of the given string is : {length_of_strng}")

#3

count_the = ent_string.count("the")

print(f"Count of the word 'the' in the given string is : {count_the}")

#4

punctuation_mark = (".",",","!","?")
end_punch = ent_string.endswith(punctuation_mark)

print(f"contains punctuation marks: {end_punch}")

#5

modified_string = ent_string.replace(" ","_")
print(f"replaced string : {modified_string}")

#6

splited_string = ent_string.split(" ")[0]
print(f"Extracted first word from the given string: {splited_string} ")
