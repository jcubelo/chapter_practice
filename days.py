Monday = 1
Tuesday = 2
Wedesday = 3
Thursday = 4
Friday = 5
Saturday = 6
Sunday = 7

day = int(input("Enter a number 1-7: "))
if day == Monday:
    print("Monday")
elif day == Tuesday:
    print("Tuesday")
elif day == Wedesday:
    print("Wednesday")
elif day == Thursday:
    print("Thursday")
elif day == Friday:
    print("Friday")
elif day == Saturday:
    print("Saturday")
elif day == Sunday:
    print("Sunday")
elif day > 7 or day < 1:
    input("Enter a number between 1 and 7 please: ")
