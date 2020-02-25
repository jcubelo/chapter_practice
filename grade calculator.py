def calcAverage(score1, score2, score3, score4, score5):
    average= (score1 + score2 + score3 + score4 + score5)/5
    return average
def determineGrade(userscore):
    if(userscore < 60):
        return "F"
    elif(userscore < 70):
        return "D"
    elif(userscore < 80):
        return "C"
    elif(userscore < 90):
        return "B"
    elif(userscore < 101):
        return "A"
def askForScore():
    score1 = float(input("Please enter score 1: "))
    score2 = float(input("Please enter score 2: "))
    score3 = float(input("Please enter score 3: "))
    score4 = float(input("Please enter score 4: "))
    score5 = float(input("Please enter score 5: "))
    return score1, score2, score3, score4, score5
def tableofresults(score1, score2, score3, score4, score5):
    print("Score\tLetter Grade")
    print(str(score1) + "\t" + determineGrade(score1))
    print(str(score2) + "\t" + determineGrade(score2))
    print(str(score3) + "\t" + determineGrade(score3))
    print(str(score4) + "\t" + determineGrade(score4))
    print(str(score5) + "\t" + determineGrade(score5))
def main():
    score_tuple=askForScore()
    score1, score2, score3, score4, score5=score_tuple[0],score_tuple[1],score_tuple[2],score_tuple[3],score_tuple[4]
    tableofresults(score1, score2, score3, score4, score5)
    print( "Your average is", calcAverage( score1, score2, score3, score4, score5 ) )
main()

