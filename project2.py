#creates lists
nouns = []
verbs = []
adjs = []

#functions make list
def nounlist():#these r the nouns in the story
    global nouns
    for i in range(4): 
        nouns.append(input("gimmie a noun ")) #asks player for nouns

def verblist():#verbs in the story
    global verbs
    for i in range(3): 
        verbs.append(input("give a verb ending in ed ")) #asks user for verbs

def adjlist():#these are the adjectives in story
    global adjs
    for i in range(2): 
        adjs.append(input("gimmie an adjective ")) #asks for adjectives

#sorts the inputs and gives them the order for the story
def theinputs():
    global words
    words = [nouns[0], nouns[1], verbs[0], verbs[1], nouns[2],
              adjs[0], adjs[1], nouns[3], verbs[2]]

#list w/ starters and endsers 
def phrases():
    global starters, enders
    starters = ["One day I went to the ","My family rode in the ","We ",
            "Then we ","At the place I saw a ","It was very ",
            "Everything looked ","The best thing was the ","Before leaving we "]
    enders = [".",".",".",".",".",".",".",".","."]

#this one matches the starter with the fill in then the ender
def story():
    global starters, enders, words
    print(" ")
    for i in range(len(words)):
        phrase = starters[i] + words[i] + enders[i]
        print(phrase)

#prompts to go again
def replay(answer):
    if answer.lower() == "no":
        print("")
        print("")
        print("")
        print("funny huh, bye")
    elif answer.lower() == "yes":
        verbs.clear()
        adjs.clear()
        nouns.clear()
        print(" ")
        print(" ")
        print(" ")
        run()
    else:
        play = input("one more round? yes or no? ")
        replay(play)

        
        
    
        


#runs all the differnt functions
def run():
    nounlist()  
    verblist()
    adjlist()
    theinputs()
    phrases()
    story()
    play = input("one more round? yes or no? ")
    replay(play) #runs the players answer

run()