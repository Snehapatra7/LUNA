# Function to check if a number is even or odd
def check_even_odd(num):
    if num % 2 == 0:
        return f"{num} is Even"
    else:
        return f"{num} is Odd"

# Taking user input
number = int(input("Enter a number: "))
result = check_even_odd(number)
print(result)
