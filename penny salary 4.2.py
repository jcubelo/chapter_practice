numworkdays = int(input("Please enter how many days worked: "))
totalpennies = 0
print("----------")
print( "Day\tSalary\n---\t------" )
for currday in range( numworkdays ):
    pennyperday = 2**currday
    totalpennies += pennyperday
    print( currday + 1, "\t" , pennyperday)
totalpay = totalpennies * .01
print( "\nTotal pay: ", totalpay )
