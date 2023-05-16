import random




def rounding():
    while True:
        Roundq = input("how many rounds?: ")
        
        rounderror = "You can't do zero, maybe try -1"

    # If Infinite mode not chosen check response
    # -1 will trigger a mode where you have 3 lives and 10 rounds, if won they will get a password for a ZIPPED Folder that has pictures of plants
    
        if Roundq == "":
            print("you did nothing, you did not deserve to press ENTER")
        else:
            return Roundq
        
def choose_item(question, valid_list, error):

    # Ask user for choice (and transform them into lowercase)
    valid = False
    while not valid:
    # 
        response = input(question).lower()

        for item in valid_list:
            if response == item[0] or == item:
                return item
        print(error)
        print()

def instructions():
    print()
    print("**** How to Play ****")
    print()
    print("Choose either a number of rounds or "
          "press <enter> for infinite mode")
    print()
    print("then for each round pick rock, paper or scissors(or XXX to quit)")
    print()
    print("the ruiles are...\n"
          "Rock beats scissors\n"
          " Scissors beats paper\n"
          " Paper beats rock")
    print()
    print("*** Have fun ***")
 
def gameplay():

 