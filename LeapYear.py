year = int(input("Enter a year: "))

#if statement used to determine if year is in the Gregorian calendar period which begain in 1582
#elif statements used to determine if year is divisible by 4, 100, 400 to determine if leap or common year


if year < 1582:
    print("Not within the Gregorian calendar period")
elif year % 4 != 0:
    print("Common year")
elif year % 100 != 0:
    print("Leap year")
elif year % 400 != 0:
    print("Common year")
else:
    print("Leap year")
