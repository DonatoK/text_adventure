def newFunction(option):
    # notice I am passing something and reading whats returned. This can be
    # useful for putting different chapters of your story in modules and having
    # them keep track of how your story is progressing

    # Expand with all types of options here, be creative! pay attention to how
    # different the code looks vs what you see in the terminal. The person you
    # share your game with will not see your code when interacting with it.

    # you can ask things like math questions and make choices on if the user gets
    # it right or not.s
    print("The user input:", option)
    localUserInput = input("please enter something new")
    print(localUserInput)
    # getting  a user input using a 3 option function
    optionList = ["cup", "orange", "banana"]
    # before calling threeOptions make sure to print out the question for the user
    print("There are three things on the table what would you like?")
    checkInput = 1

    while(checkInput):
        localUserInput = threeOptions(optionList)
        if(localUserInput == "1"):
            print("the first option")
            checkInput = 0
        elif(localUserInput == "2"):
            print("the second option")
            checkInput = 0
        elif(localUserInput == "3"):
            print("the third option")
            checkInput = 0
        else:
            print("enter the correct value")
    conditionList = ["1", "2", "3"]
    localUserInput = threeConditions(conditionList, optionList)
    # Printing the prompt before and the result after allows for function reuse
    return localUserInput


def threeConditions(conditions, optionList):
    endloop = 1
    localUserInput = threeOptions(optionList)
    while(endloop):
        if(localUserInput == conditions[0]):
            print("the first option")
            endloop = 0
        elif(localUserInput == conditions[1]):
            print("the second option")
            endloop = 0
        elif(localUserInput == conditions[2]):
            print("the third option")
            endloop = 0
        else:
            print("enter the correct value")


def threeOptions(threeItemList):
    # this function will take in a 3 item list, display the options, ask a User
    # For an input and return the selected option
    print(threeItemList[0], ": 1\n", threeItemList[1],
          ": 2\n", threeItemList[2], ": 3\n")
    userSelection = input()
    return userSelection
