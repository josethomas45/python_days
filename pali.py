def is_palindrome(n):
    original = n
    reversed_num = 0

    while n > 0:
        digit = n % 10
        reversed_num = reversed_num * 10 + digit
        n //= 10

    return original == reversed_num

while True:
    num = input("Enter a number (or type 'exit' to quit): ")

    if num.lower() == 'exit':
        print("Goodbye! 👋")
        break

    if num.isdigit():
        num = int(num)
        if is_palindrome(num):
            print("✅ It's a palindrome!")
        else:
            print("❌ Not a palindrome.")
    else:
        print("⚠️ Invalid input! Please enter a valid number.")
