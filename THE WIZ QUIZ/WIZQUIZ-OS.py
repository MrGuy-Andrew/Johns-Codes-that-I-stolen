# Wizard Quiz, but it is very mundane and average

# the Questions Tuples - From [0] to [14]
Question = (
    # Question 1
    "What is the average wizard's favorite hot beverage?",

    # Question 2
    "Which type of broomstick is commonly used by wizards for everyday chores?",

    # Question 3
    "What is the most common color for a wizard's hat?",

    # Question 4
    "What do wizards usually use to fix minor household repairs?",

    # Question 5
    "What is the primary ingredient in a wizard's basic cleaning potion?",
)

# the Options Tuples - each question gets 4 of these options
Options = (
    # Question 1 - What is the average wizard's favorite hot beverage?
    ("Coffee", "Tea", "Hot cocoa", "Herbal infusion"), 

    # Question 2 - Which type of broomstick is commonly used by wizards for everyday chores?   
    ("Oak handle broomstick", "Willow twig broomstick", "Bamboo sweep broomstick", "Birchwood broomstick"), 

    # Question 3 - What is the most common color for a wizard's hat?
    ("Emerald green", "Deep blue", "Black", "Dark purple"), 

    # Question 4 - What do wizards usually use to fix minor household repairs?
    ("Spellbound glue", "Magical adhesive tape", "Enchanted screws", "Repairing charms"),

    # Question 5 - What is the primary ingredient in a wizard's basic cleaning potion?
    ("Unicorn horn shavings", "Dragon scale powder", "Pixie wing dust", "Basilisk fang essence"), 
)

def Questquest():
    WIZscore = [0, 0, 0, 0, 0]

    def quest0():
        # Question 1
        question = Question[0]
        options = Options[0]
        print(question)
        print(options)
        userput = int(input())
        if userput == 2:
            WIZscore[0] = 1

    def quest1():
        # Question 2
        question = Question[1]
        options = Options[1]
        print(question)
        print(options)
        userput = int(input())
        if userput == 4:
            WIZscore[1] = 1

    def quest2():
        # Question 3
        question = Question[2]
        options = Options[2]
        print(question)
        print(options)
        userput = int(input())
        if userput == 3:
            WIZscore[2] = 1

    def quest3():
        # Question 4
        question = Question[3]
        options = Options[3]
        print(question)
        print(options)
        userput = int(input())
        if userput == 2:
            WIZscore[3] = 1

    def quest4():
        # Question 5
        question = Question[4]
        options = Options[4]
        print(question)
        print(options)
        userput = int(input())
        if userput == 2:
            WIZscore[4] = 1

    quest0()
    quest1()
    quest2()
    quest3()
    quest4()

    def WIZcal():
        WIZfinal = sum(WIZscore)
        WIZfinal1 = round(WIZfinal * 20)
        print(f"{WIZfinal1}% out of 5")

    def questpop():
        again = input("Do you want to try again on this magical thing called a computer game? \n[ Yes / Sure / Absolutely / Of course / Yeah / Y / Yay / Yea / Definitely / Affirmative ] ")
        if again.lower() in ["yes", "sure", "absolutely", "of course", "yeah", "y", "yay", "yea", "definitely", "affirmative"]:
            Questquest()

    WIZcal()

    questpop()

Questquest()