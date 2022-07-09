# This code is a small adventure of my cats day.
# by Donato Kava



def peppers_day():
    peppers_health = 100
    bug_health = 100
    damage = 1
    # game module 1 = games longest play through
    # game moduel 2 = game ended early
    print("""Pepper is a black cat and expert bug hunter...

            you are a stink bug...

            Survive!!!""")
    print("--------------------------------------------------")
    input("press enter to continue")

    print("""Stinkbug: You wake up on a wall, time to go do stink bug things,
              your favorite. Makes you think back to the way your stink bug mom
              would always tell you, first she would shout...""")

    userNAME= input("enter your name")
    print("Wait, she called you ",userNAME, "?")

    userInput=input("Y?, N?")

    if(userInput == ("N" or "n")):
        print("So what did she call you?")
        while (userInput != "Y" or "y"):
            print("So what did she call you?")
            userNAME= input("enter your name")
            print("Wait, she called you ",userNAME, "?")
            userInput=input("Y?, N?")

    print("okay your mom would say ", userNAME,"""! You know stink bug life is
           mostly about being the most annoying thing inside a house it can
           be hard or it can be easy!""")

    print("How difficult do you want this game to be?")
    print("Easy")  #baseline
    print("Hard")  #multiply extreme
    print("EXTREME!!") # game ends

    userInput=input()
    #check for proper user userInput
    while(userInput != ("Easy" or "Hard" or "EXTREME" or "EXTREME!!") ):
        print("check answer format: Easy, Hard, EXTREME")
        userInput=input()
    print("Wow",userInput)
    if(userInput == "Hard"):
        damage = 10
    elif(userInput == ("EXTREME" or "EXTREME!!")):
        # ends the function early with a quick death
        print("bug life cant handle pepper at her best, she sees you and eats you")
        print("game over!")
        game_module_over = 2
        return game_module_over # ends the function early with a quick death

    print("you ", userNAME, """a stinkbug start to move, pepper notices,
    the fight is on.
    Do you run or do you fight?""")
    while (bug_health >= 0):
        userInput = input("run?, fight?")
        while(userInput != ("run" or "fight") ):
            print("check answer format: run, fight")
            userInput=input()
        if(userInput == "run"):
            bug_health = bug_health - damage
            print("it was wise to run, pepper moves to attack and only hits your leg")
            print("your lifepoints are now: ", bug_health)
            print("peper's lifepoints is now: ", peppers_health)
        if(userInput == "fight"):
            bug_health = bug_health - (damage *10)
            print("it was unwise to fight, pepper doesnt play and the damage is is heavy")
            print("your lifepoints are now: ", bug_health)
            print("peper's lifepoints is now: ", peppers_health)
        print("what would you like to do now?")
    print ("good try but pepper is an expert stink bug hunter")
    game_module_over = 1
    return game_module_over
