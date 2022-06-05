# This file is for the functions that are called all the time in the story

def threeConditions(conditions, optionList):
    endloop = 1
    localUserInput = threeOptions(optionList)
    # THis is the threeoptions function. Notice the changes required to make it
    # work here vs how it works in its function.
    #print(optionList[0], ": 1\n", optionList[1],
    #      ": 2\n", optionList[2], ": 3\n")
    #localUserInput = input()

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
