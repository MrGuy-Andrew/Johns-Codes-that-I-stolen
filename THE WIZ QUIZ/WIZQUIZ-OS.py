
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
    

    # Question 6
    "Which creature is often kept as a pet by wizards due to its ability to chase away mice?",


    # Question 7
    "What type of pen do wizards typically use for writing magical notes?",


    # Question 8
    "What is the preferred attire for wizards during a casual gathering?",


    # Question 9
    "What do wizards typically use to stir their magical concoctions?",


    # Question 10
    "Which plant is commonly found in a wizard's garden for its healing properties?",


    # Question 11
    "What is the main tool used by wizards to extinguish small fires?",


    # Question 12
    "What is the preferred method for wizards to organize their magical book collection?",


    # Question 13
    "Which spell is commonly used by wizards to locate lost objects?",


    # Question 14
    "What is the staple food item in a wizard's pantry?",


    # Question 15
    "What is the preferred mode of transportation for wizards on short trips?"

)

# the Options Tuples - each question gets 4 of these options
Options = (

    # Question 1 - What is the average wizard's favorite hot beverage?
    ("Tea", "Coffee", "Hot cocoa", "Herbal infusion"), 


    # Question 2 - Which type of broomstick is commonly used by wizards for everyday chores?   
    ("Birchwood broomstick", "Willow twig broomstick", "Oak handle broomstick", "Bamboo sweep broomstick"), 


    # Question 3 - What is the most common color for a wizard's hat?
    ("Black", "Deep blue", "Dark purple", "Emerald green"), 


    # Question 4 - What do wizards usually use to fix minor household repairs?
    ("Magical adhesive tape", "Enchanted screws", "Spellbound glue", "Repairing charms"),


    # Question 5 - What is the primary ingredient in a wizard's basic cleaning potion?
    ("Dragon scale powder", "Unicorn horn shavings", "Pixie wing dust", "Basilisk fang essence"), 


    # Question 6 - Which creature is often kept as a pet by wizards due to its ability to chase away mice?
    ("Pygmy Puff", "Kneazle", "Bowtruckle", "Knarl"), 


    # Question 7 - What type of pen do wizards typically use for writing magical notes?
    ("Quill made from phoenix feathers", "Wand-shaped ink pen", "Crystal quill", "Silver fountain pen"), 


    # Question 8 - What is the preferred attire for wizards during a casual gathering?
    ("Robes with colorful patterns", "Elegant waistcoats with matching trousers", "Flowing tunics with embroidered designs", "Velvet jackets with jeweled buttons"), 


    # Question 9 - What do wizards typically use to stir their magical concoctions?
    ("Wooden spoon carved from elderwood", "Silver-plated wand with a curved handle", "Copper stirring rod engraved with symbols", "Glass rod filled with liquid magic"),


    # Question 10 - Which plant is commonly found in a wizard's garden for its healing properties?
    ("Gillyweed", "Mandrake", "Aconite (Wolfsbane)", "Valerian root"), 


    # Question 11 - What is the main tool used by wizards to extinguish small fires?
    ("A charm that instantly removes oxygen from the area", "A handheld device that emits a cooling mist", "Water-filled enchanted goblet", "Fire-freezing spray"), 


    # Question 12 - What is the preferred method for wizards to organize their magical book collection?
    ("Alphabetical order by title", "Categorized by magical discipline", "Sorting by author's last name", "Arranged chronologically by publication date"), 


    # Question 13 - Which spell is commonly used by wizards to locate lost objects?
    ("Accio", "Revelio", "Lumos Solem", "Homenum Revelio"), 


    # Question 14 - What is the staple food item in a wizard's pantry?
    ("Pumpkin pasties", "Chocolate frogs", "Cauldron cakes", "Honeydukes' fudge"), 


    # Question 15 - What is the preferred mode of transportation for wizards on short trips?
    ("Broomstick", "Floo Powder", "Apparition", "Portkey")) 
    
# The Options will be formatted by A1 to O4
# Example will be "What is the most common color for a wizard's hat?" which will be linked to a variable 
# called 'C' and the options will have 'C1', 'C2', 'C3' and 'C4' for input reason

# It will use a 'If' and 'Else' command for each questions, for example on 'C', if they chosen "Black" which 
# equates to 'C1', and it will use a 'If x == y:' with another tuple for the answers to see if they are the same,
# if it's the same then it will add '6.666666667', if not then it will not add then
# 

correct_answers = (

    # Question 1 - What is the average wizard's favorite hot beverage?
    "Tea", 


    # Question 2 - Which type of broomstick is commonly used by wizards for everyday chores? 
    "Birchwood broomstick",


    # Question 3 - What is the most common color for a wizard's hat?
    "Black",


    # Question 4 - What do wizards usually use to fix minor household repairs?
    "Magical adhesive tape",


    # Question 5 - What is the primary ingredient in a wizard's basic cleaning potion?
    "Dragon scale powder",


    # Question 6 - Which creature is often kept as a pet by wizards due to its ability to chase away mice?
    "Kneazle",


    # Question 7 - What type of pen do wizards typically use for writing magical notes?
    "Quill made from phoenix feathers",


    # Question 8 - What is the preferred attire for wizards during a casual gathering?
    "Robes with colorful patterns",


    # Question 9 - What do wizards typically use to stir their magical concoctions?
    "Silver-plated wand with a curved handle",


    # Question 10 - Which plant is commonly found in a wizard's garden for its healing properties?
    "Gillyweed",


    # Question 11 - What is the main tool used by wizards to extinguish small fires?
    "A charm that instantly removes oxygen from the area",


    # Question 12 - What is the preferred method for wizards to organize their magical book collection?
    "Categorized by magical discipline",


    # Question 13 - Which spell is commonly used by wizards to locate lost objects?
    "Accio",


    # Question 14 - What is the staple food item in a wizard's pantry?
    "Pumpkin pasties",


    # Question 15 - What is the preferred mode of transportation for wizards on short trips?
    "Broomstick"

)


def Questquest():

    WIZscore = [1,1,1,1,1,1,1,1,1,1,1,1,1,1,1]

    def quest0():
        question = Question[0]
        options = Options[0]
        print(question)
        print(options)
        userput = int(input())
        if userput == 1:
            WIZscore[2] = 1
        else:
            WIZscore[2] = 0
    def quest1():
        question = Question[1]
        options = Options[1]
        print(question)
        print(options)
        userput = int(input())
        if userput == 1:
            WIZscore[2] = 1
        else:
            WIZscore[2] = 0
    def quest2():
        question = Question[1]
        options = Options[1]
        print(question)
        print(options)
        userput = int(input())
        if userput == 1:
            WIZscore[2] = 1
        else:
            WIZscore[2] = 0
    def quest3():
        question = Question[1]
        options = Options[1]
        print(question)
        print(options)
        userput = int(input())
        if userput == 1:
            WIZscore[2] = 1
        else:
            WIZscore[2] = 0
    def quest4():
        question = Question[0]
        options = Options[0]
        print(question)
        print(options)
        userput = int(input())
        if userput == 1:
            WIZscore[2] = 1
        else:
            WIZscore[2] = 0
    def quest5():
        question = Question[1]
        options = Options[1]
        print(question)
        print(options)
        userput = int(input())
        if userput == 1:
            WIZscore[2] = 1
        else:
            WIZscore[2] = 0
    def quest6():
        question = Question[2]
        options = Options[2]
        print(question)
        print(options)
        userput = int(input())
        if userput == 1:
            WIZscore[2] = 1
        else:
            WIZscore[2] = 0
    def quest7():
        question = Question[3]
        options = Options[3]
        print(question)
        print(options)
        userput = int(input())
        if userput == 1:
            WIZscore[2] = 1
        else:
            WIZscore[2] = 0
    def quest8():
        question = Question[4]
        options = Options[4]
        print(question)
        print(options)
        userput = int(input())
        if userput == 1:
            WIZscore[2] = 1
        else:
            WIZscore[2] = 0
    def quest9():
        question = Question[5]
        options = Options[5]
        print(question)
        print(options)
        userput = int(input())
        if userput == 1:
            WIZscore[2] = 1
        else:
            WIZscore[2] = 0
    def quest10():
        question = Question[6]
        options = Options[6]
        print(question)
        print(options)
        userput = int(input())
        if userput == 1:
            WIZscore[2] = 1
        else:
            WIZscore[2] = 0
    def quest11():
        question = Question[7]
        options = Options[7]
        print(question)
        print(options)
        userput = int(input())
        if userput == 1:
            WIZscore[2] = 1
        else:
            WIZscore[2] = 0
    def quest12():
        question = Question[8]
        options = Options[8]
        print(question)
        print(options)
        userput = int(input())
        if userput == 1:
            WIZscore[2] = 1
        else:
            WIZscore[2] = 0
    def quest13():
        question = Question[9]
        options = Options[9]
        print(question)
        print(options)
        userput = int(input())
        if userput == 1:
            WIZscore[2] = 1
        else:
            WIZscore[2] = 0
    def quest14():
        question = Question[10]
        options = Options[10]
        print(question)
        print(options)
        userput = int(input())
        if userput == 1:
            WIZscore[2] = 1
        else:
            WIZscore[2] = 0
    
    quest0()
    quest1()
    quest2()
    quest3()
    quest4()
    quest5()
    quest6()
    quest7()
    quest8()
    quest9()
    quest10()
    quest11()
    quest12()
    quest13()
    quest14()

    def WIZcal():
        WIZfinal = WIZscore[0] + WIZscore[1] + WIZscore[2] + WIZscore[3] + WIZscore[4] + WIZscore[5] + WIZscore[6] + WIZscore[7] + WIZscore[8] + WIZscore[9] + WIZscore[10] + WIZscore[11] + WIZscore[12] + WIZscore[13] + WIZscore[14]

                
        WIZfinal1 = round(WIZfinal * 6.666666667,0)
        print(f"{WIZfinal1}%")

    def quest23():
        Questquest()

        
    
    WIZcal()
    

    
Questquest()

