nummonths = 0
totalrainfall = 0
numyears = int(input("How many years would you like to collect data for? :"))
for curryear in range( 1, numyears + 1):
    for currmonth in range (1,13):
        monthlyrain = float(input("Please type the inches of" + \
            " rainfall for month " + format(currmonth, "d") + ": "))
        totalrainfall += monthlyrain
        nummonths += 1
averagerain = totalrainfall / nummonths
print("Number of months: " + format(nummonths, "d"), "Total" + \
      " inches of rainfall: " + format(totalrainfall, ".2f"), \
      "Average rainfall: " +format(averagerain, ".2f" ), sep="\n")

