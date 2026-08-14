Age = int(input("Please enter your current age:"))

if Age < 0:
    print("You have entered an invalid age. Please enter a valid age.")
elif Age <= 3:
    print("You are a toddler.")
elif Age <= 6:
    print("You are a child.")
elif Age <= 13:
    print("You are a teenager.")
elif Age <= 20:
    print("You are a young adult.")
elif Age <= 65:
    print("You are a senior citizen.")