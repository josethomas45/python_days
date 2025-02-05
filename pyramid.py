def pyramid(limit):
    for i in range(1, limit+1):
        print(""*(limit-i) +"*" *(2*i-1))

limit = int(input("Enter the number of stars:"))
pyramid(limit)

