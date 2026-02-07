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

def ScenarioMain():
    print("You have a big Comp Sci test today and you want to get out of school.")
    #this is the main scenario, where you choose your path
    showStats()

    print("The bell is about to ring.")
    print("1: Go to the nurse and fake sick")
    print("2: Try to leave at lunch")
    print("3: Talk to the teacher")
    choice = int(input("Choose 1, 2, or 3: "))

    if choice == 1:
        Scenario1()
    elif choice == 2:
        Scenario2()
    elif choice == 3:
        Scenario3()
    else:
        print("Invalid choice. Try again.")
        ScenarioMain()


# Different Scenarios

def Scenario1():
    # path 1
    global stress
    global timeLeft
    timeLeft = timeLeft - 2
    stress = stress + 2
    showStats()
    print("Scenario 1: You're in the nurse office.")
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
        Scenario1()


def Scenario2():
    # path 3
    global timeLeft
    timeLeft = timeLeft - 2
    showStats()

    print("Scenario 3: It's lunch. The exits are crowded.")
    print("1: Sneak out quickly")
    print("2: Wait for a distraction")
    choice = int(input("Choose 1 or 2: "))

    if choice == 1:
        Scenario7()
    elif choice == 2:
        timeLeft = timeLeft - 1
        checkScore ()
    else:
        print("Invalid choice. Try again.")
        Scenario3()

def Scenario3():
    global timeLeft
    global stress
    stress = stress + 2
    timeLeft = timeLeft - 1
    showStats()

    print("Scenario 4: You talk to the teacher before class.")
    print("1: Be honest")
    print("2: Make up an excuse")
    choice = int(input("Choose 1 or 2: "))

    if choice == 1:
        stress = stress - 1
        print("\nThe teacher understands and lets you take the test another day.")
        checkScore()
    elif choice == 2:
        stress = stress + 3
        print("\nThe teacher does not believe you. You sit down... test time.")
        checkScore()
    else:
        print("Invalid choice. Try again.")
        Scenario3()


def Scenario7():
    # path 
    global stress
    global timeLeft
    stress = stress + 2
    showStats()
    print("Scenario 7: Security is near the exit.")
    print("1: Walk past confidently")
    print("2: Turn around and try another way")
    choice = int(input("Choose 1 or 2: "))
    if choice == 1:
        # security catches you
        stress = stress + 2
        timeLeft = timeLeft + 3
        checkScore()
    elif choice == 2:
        # you sneak another way
        stress = stress + 1
        timeLeft = timeLeft - 1
        checkScore()
    else:
        print("Invalid choice. Try again.")
        Scenario7()

#this is the thing that prints if you won or lost
def endGame(result):
    print("\n--- GAME OVER ---")
    if result == True:
        print("You escaped the test (or delayed it lol)")
        print("Final stress =", stress)
        print("Final timeLeft =", timeLeft)
    else:
        print("You did not escape the test.")
        print("Final stress =", stress)
        print("Final timeLeft =", timeLeft)

ScenarioMain()
