# This is a starter for a text based game in python.
# fill it in and tell a story that would be fun to play

from expand import *
# I use multiple modules as an example for you to try and replicate to keep your
# story neat and get used to using them

# Basic control flow is what this file mostly deals with and the end goal is
# to let others use it. Try to make your code so it doesn’t break easily.


def main():
   # end story is the variable I will use to end the program.
   endStory = 2
   # The while loop will keep repeating until the break of set by endStory is
   # triggered
   while(endStory > 1):
       # terminal prints can be over multiple lines using """ print """ format,
       # instead of the regular  "print" give it a try
       print("this is the start of a story, You could pass things to main to include multiple items")
       # this is how your story can take input and read it back out
       userInput = input("Please enter something: ")
       print("user input: ", userInput)
       # notice input can output to terminal. Look up the input function for python
       # to see why.
       userInput = input("""neat, now enter something from the choices i give you
                 option 1: enter a F to end
                 option 2: enter a C to continue """)
       # there are many ways to break this and you should try to write code that
       # catches common cases and check the user for options other than what
       # asked for.
       if(userInput == "C"):
           print("into the expanded module this code will go")
           moduleReturns = newFunction(userInput)
           print("wow you really put ", moduleReturns)
           print("goodbye, rerun python main.py to play")
# This ends the story
           endStory = 0
       elif(userInput == "F"):
           print("goodbye, rerun python main.py to play")
# This also ends the story
           endStory = 0

       print("the option was case sensitive or you didn't selected from per-determined options")


# Remove this and try to run your code to try and understand what it does so
# if you write a main module and its not working you can tell why.
if __name__ == '__main__':
    main()
