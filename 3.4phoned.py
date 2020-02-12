###Package A: For $39.99 per month 450 minutes are provided. Additional minutes are $0.45 per minute.
###Package B: For $59.99 per month 900 minutes are provided. Additional minutes are $0.40 per minute.
###Package C: For $69.99 per month unlimited minutes provided.
x = input("Which phone plan do you have (A, B, or C)?: ")
y = int(input("How many minutes did you use?: "))
a = 39.99
ra = .45
b = 59.99
rb = .40
c = 69.99
amins = 450
bmins = 900
cost = 39.99
if x == a:
    if y <= amins:
        cost = 39.99
    elif y >> amins:
        cost = 39.99 + .45*(y - 450)
if x == b:
    cost = 59.99
    if y <= bmins:
        cost = 59.99
    elif y >> bmins:
        cost = 59.99 + .40*(y - 900)
print("With package " + str(x) + " and " + str(y) + " minutes, you owe " + str(cost))
