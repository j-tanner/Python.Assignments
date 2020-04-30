largest = None
smallest = None

while True:
    user_input = input("Enter a number: ")
    if user_input == "done":
        break
    try:
        converted_number = int(user_input)
    except:
        print("Invalid input")
        continue

    if largest is None or converted_number > largest:
        largest = converted_number
    if smallest is None or converted_number < smallest:
        smallest = converted_number

print("Maximum is", largest)
print("Minimum is", smallest)
