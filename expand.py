from functions import *


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

def three_option_choice(choiceList):
    # this function takes a list of 3 options, prints them and returns the selected one
    return nothing
