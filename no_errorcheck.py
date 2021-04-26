import sys # implements command-line arguments so code doesn't have to be modified

def leap_years(n):
    if n % 4 == 0:
        if n % 100 != 0:
            print("leap year!")
        elif n % 400 == 0:
            print("that's a leap year!")
        else:
            print("that's not a leap year")

leap_years(int(sys.argv[1]))