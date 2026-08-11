print("Select your ride:")
print("1. Bike")
print("2. Car")

choice = int(input("Enter your choice. Make sure to enter 1 or 2: "))

if( choice == 1 ):
    print("What type of bike do you prefer?")
    print("1. Scooty\n")
    print("2. Sports Bike\n")

    choice2 = int(input("Enter your choice2:"))
    if choice2==1:
        print("You have selected Scooty.")
    else:
        print("You have selected Sports Bike.")

elif (choice == 2):
    print("What type of car do you prefer?")
    print("1. Sedan")
    print("2. SUV")
    choice3 = int(input("Enter your choice3:"))

    if choice3 == 1:
        print("You have selected Sedan.")
    else:
        print("You have selected SUV.")

else:
    print("Invalid choice. Please select either 1 or 2.")