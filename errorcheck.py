def leap_years(n):
    if n % 4 == 0:
        if n % 100 != 0:
            print("leap year!")
        elif n % 400 == 0:
            print("that's a leap year!")
        else:
            print("that's not a leap year")
    else:
        print("that's not a leap year")


year = input("Give me a positive integer and I'll tell you if it's a leap year: ")
checking = True

while checking:
    if(type(year) == int and year > 0):
        leap_years(year)
        checking = False
    else:
        year = int(input("Try again, that was not a valid number: "))
