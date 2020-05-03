largest = None
smallest = None


while True:
    inp = raw_input("Enter a number: ")
    if inp == "done": break
    try:
        num = int(inp)
    except:
        print("Invalid input")
    else:
        if smallest is None:
            smallest = num
        if largest is None:
            largest = num
        elif num > largest:
            largest = num
        elif num < smallest:
            smallest = num


print("Maximum is", largest)
print("Minimum is", smallest)
