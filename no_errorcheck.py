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


leap_years(input("Give me a positive integer and I'll tell you if it's a leap year: "))
