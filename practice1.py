year = int(input("Current year: "))
a = int(input("Enter your age/year of birth: "))
isAge = False
isYear = False
if len(str(a)) == 4:
    isYear = True
else:
    isAge = True
if a < 1900 and isYear:
    print("You seem to be the oldest person alive!")
    exit()
if a > year:
    print("You are not born yet")
    exit()
if isAge:
    a = year - a
print(f"In {a + 100} you will be 100 years old.")

optYr = int(input("Enter the year you want to know your age in: "))
print(f"You will be {optYr - a} years old in {optYr}")
