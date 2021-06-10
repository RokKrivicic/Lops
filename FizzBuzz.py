choice = int(input("Select a number between 1 and 100: "))

for x in range(choice):

    if (x+1)%3 == 0 and (x+1)%5 == 0:
        print("fizzbuzz")
    elif(x+1)%5 == 0:
        print("buzz")
    elif (x + 1) % 3 == 0:
        print("fizz")
    else:
        print(x+1)
