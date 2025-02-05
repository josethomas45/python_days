
data = "Python rules!"

words_list = data.split()
print("List of words:", words_list)

uppercase_data = data.upper()
print("Uppercase string:", uppercase_data)

position = data.find("rules")
if position != -1:
    print('The substring "rules" is found at index:', position)
else:
    print('The substring "rules" is not found.')

replaced_data = data.replace('!', '?')
print("Modified string:", replaced_data)
