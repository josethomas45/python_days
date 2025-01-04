num1 = int(input("Enter the first number! \n"))
num2 = int(input("Enter the second number! \n"))
product = num1 * num2
sum = num1 + num2
if product < 1000:
    print(f" The product of {num1} and {num2} is {product} and its les than 1000 ")
else:
    print(f"The sum of {num1} and {num2} is {sum} because the product is greater than 1000")
