def convert_to_celsius(fahrenheit):
    return (fahrenheit - 32) * 5.0/9.0

def convert_to_fahrenheit(celsius):
    return (celsius * 9.0/5.0) + 32

def main():
    print("Temperature Conversion")
    print("1. Fahrenheit to Celsius")
    print("2. Celsius to Fahrenheit")
    choice = int(input("Enter your choice: "))

    if choice == 1:
        fahrenheit = float(input("Enter temperature in Fahrenheit: "))
        celsius = convert_to_celsius(fahrenheit)
        print(f"Temperature in Celsius: {celsius}")
    elif choice == 2:
        celsius = float(input("Enter temperature in Celsius: "))
        fahrenheit = convert_to_fahrenheit(celsius)
        print(f"Temperature in Fahrenheit: {fahrenheit}")
    else:
        print("Invalid choice.")




