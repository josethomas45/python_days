import hashlib 

with open("pythonji.txt", "r") as file:
    content =  file.read()
    hash_value = hashlib.sha512(content.encode()).hexdigest()
    print(f'Content inside the file {content}')
    print(f'hash value of the file : {hash_value}')
