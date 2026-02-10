# Escape the test game 

stress = 5
timeLeft = 3

def showStats():
    print("\nStats:")
    print("stress =", stress)
    print("time left =", timeLeft)

def checkScore():
    if timeLeft <= 0:
        #run out of time
        print("\nTime ran out. The test starts.")
        endGame(False)
        return
    elif stress >= 10:
        # too stressed
        print("\nYou panic too much and can't escape.")
        endGame(False)
        return
    else:
        # you win!
        endGame(True)
        return

def Start():
    print("You have a Comp Sci test today and you wanna skip it.")
    #this is the main scenario, where you choose your path
    showStats()
    print("The bell is about to ring.")
    print("1: Go to the nurse and fake sick")
    print("2: Try to leave at lunch")
    print("3: Talk to Ms. Tamony")
    choice = int(input("Choose 1, 2, or 3: "))
    if choice == 1:
        Nurse()
    elif choice == 2:
        Lunch()
    elif choice == 3:
        Teacher()
    else:
        print("Invalid choice. Try again.")
        Start()


# Different Scenarios

def Nurse():
    # path 1
    global stress
    global timeLeft
    timeLeft = timeLeft - 2
    stress = stress + 2
    showStats()
    print("You're in the nurse office.")
    print("The nurse looks suspicious.")
    print("1: Commit to the lie")
    print("2: Admit you're anxious")
    choice = int(input("Choose 1 or 2: "))
    if choice == 1:
        # nice you got out
        print("\nThe nurse calls your parents. You get sent home.")
        timeLeft = timeLeft + 2
        stress = stress - 4
        checkScore()
    elif choice == 2:
        # oof back to class
        print("\nThe nurse sends you back to class.")
        timeLeft = timeLeft - 1
        stress = stress + 3
        checkScore()
    else:
        print("Invalid choice. Try again.")
        Nurse()


def Lunch():
    # path 3
    global timeLeft
    global stress
    timeLeft = timeLeft - 2
    showStats()

    print("It's lunch. Coach I is by the parking lot")
    print("1: Walk out confidenly")
    print("2: Wait for a distraction")
    choice = int(input("Choose 1 or 2: "))
    if choice == 1:
        print("you make it out")
        stress=stress+2
        timeLeft=timeLeft +2
        checkScore()
    elif choice == 2:
        print("You run out of time")
        timeLeft = timeLeft - 1
        checkScore ()
    else:
        print("Invalid choice. Try again.")
        Teacher()

def Teacher():
    global timeLeft
    global stress
    stress = stress + 2
    timeLeft = timeLeft - 1
    showStats()
    print("You talk to Ms. Tamony before class.")
    print("1: Be honest")
    print("2: Make up an excuse")
    choice = int(input("Choose 1 or 2: "))
    if choice == 1:
        stress = stress - 1
        print("\nShe understands and lets you take the test another day.")
        checkScore()
    elif choice == 2:
        stress = stress + 3
        print("\nShe doesn't believe you. Test time")
        checkScore()
    else:
        print("Invalid choice. Try again.")
        Teacher()

#this is the thing that prints if you won or lost
def endGame(result):
    print("\nGAME OVER")
    if result == True:
        print("You escaped the test (or delayed it lol)")
        print("Final stress =", stress)
        print("Final timeLeft =", timeLeft)
    else:
        print("You didn't escape the test.")
        print("Final stress =", stress)
        print("Final timeLeft =", timeLeft)

Start()
