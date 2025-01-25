with open("pythonji.txt", "r") as file:
    content = file.read()
    hash_value = hash(content)
    print(f'Content inside the file {content}')
    print("Hash Value:", hash_value)
