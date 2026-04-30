#nested_if.py

num = int(input("Enter a number: "))

if num >= 0:
    if num == 0:
        print("Number is zero")
    else:
        print("Positive number")
else:
    print("Negative number")
