# Tyra's 

  #  MAPPING THE CHOICES 

# Decision 1: 
# what journey would you like to embark brave soul?
# Choice1: Middle Earth journey to find the end, Cyberpunk detective
# both choices are the same



# !!!!!!the journey begins!!!!!!!!!!!!
# Our story begins in a middle earth realm where elves, faires, dragons and magic exists
# Before we begin 


#Decision 2: Pick your clan
#Choice1: Fairy, Choice 2: Ogre, Choice 3: Wizard, Choice 4: Knight

# output fun respond ask for name 
# what is your hero name?


# Decision 3: As a {clan} in training, You work in the local pub as a busser and you overhear a 
# fellow {clan} speak of a grand adventure no one dare complete.

# Choice 3a: Ask for quest
#Choice 3b: continue bussing tables

#Decision 3a: You ask for quest. They laugh in your face. So you
#Choice 4a: Cry
#Choice 4b: Leave

#Decision 3b: You punk out and continue being a loser. The {clan} leaves, dropping a map as they stumble out of the pub.
#Choice 4c: Happily retreive it 
#Choice 4d: Deliever it back to the {clan}

# Decision 4b: You leave your shift and bump into someone. It's a wizard! You apologize perfusely he instructs you 
# you meet him on the hill @ 4:44 am for your impossible quest. What do you pack? Pick 2

# Choice 4b1: Snacks and your lucky green adventurine stone
# Choice 4b2: A sword and a extra pair of underwear

#Decision 5: You learn the quest is to reach the top of the mountain of oo. Which path will you take?
#Choice 5a: The dark path with lighting, a rickety bridge, and what appears to be a dragon stalking you.
#Choice 5b: A light path with colorful skies, fairies fluttering, and what appears to be a easy path to the mountain

# depending on your items you have chosen will determine if you make it to the mountain for the final boss
# 5a1: you have chosen -{choice 4b1} right choice
# 5a2: you have chosen -{choice 4b2} not 

# 5b1: you have chosen -{choice 4b1} not
# 5b2: you have chosen -{choice 4b2} yes


#Decision 6: You made in the top of mountain of oo. That feat is not common. You reveal the final boss...
# It is you {name} of the {clan} clan but obviously older. You are confused.
#Choice 6a: Say something first
#Choice 6b: wait

# while loop of slience oogway style

# Decision 7: You will have to answer a riddle to claim your prize.
# Choice 7a:
# 
# riddle #1 "What always runs but never walks.

# Often murmurs, never talks.

# Has a bed but never sleeps.

# An open mouth that never eats?"

# pick 2 or 3 more riddles draw them at random and you have to input the right answer
# input upper case - rejected , prompt to answer again
# right answer - you win you beat the impossible quest.. did you expect a prize

# finaldescision- choice yes or no

# yes- wrong answer. you are now a slave to the mountain and will serve until another takes ones place

# no- good choice. you win win....now leave and tell your friends to play.


# Choice 7b: failed you are like all the ones that came before you, you are exiled from the mountain 
# you shant return for 10 years


# Game over 



import inquirer


###----GLOBAL VARIABLES----
global finalBoss
finalBoss = ""
global clanDecision
clanDecision = ""
global name
name = ""
global packSupplies
packSupplies =""
hero = {
    "name": "",
    "clan": "",
}
print('')
print('')
print('')
print('')
print('')
print('')
intro = "Welcome to Tyra's adventure quest game. Be keen and clever or it's game over"


def promptIntro():
  print(intro)


def quest():
    print('')
  
    assist = [
      inquirer.List(
          'questChoose',
          message="what journey would you like to embark brave soul?",
          choices=['Middle Earth journey to find the end', 'Cyberpunk detective'],
        ),
    ]
    whichQuest = inquirer.prompt(assist)['questChoose']

    if whichQuest == 'Middle Earth journey to find the end':
        print("Great choice you are in for a treat")
    elif whichQuest == 'Cyberpunk detective':
        print("This option is unavailable. Thank you for choosing your middle earth dream")



# Select your character for your middle earth journey


def characterSelect():
  global clanDecision
  print('Our story begins in a middle earth realm where elves, faires, dragons and magic exists')
  print("")
  print('Before we begin')
  print('')
  assist = [
        inquirer.List(
            'characterSelects',
            message="Pick your clan?",
            choices=['Fairy', 'Ogre',  'Wizard', 'Knight'],
        ),
    ]

  clanDecision = inquirer.prompt(assist)['characterSelects']
    

    # Update the hero dictionary with the selected clan
  hero["clan"] = clanDecision
  
  if clanDecision == 'Fairy':
        print(f"{name} You are now a {clanDecision}! with pretty wings and sparkles that follow you everywhere...and I mean everywhere")
        print('')
  elif clanDecision == 'Ogre':
        print(f"{name} You are now a {clanDecision}! You liked Shrek growing up didn't you. It's okay this is a safe space")
        print('')
  elif clanDecision == 'Wizard':
        print(f"{name} You are now a {clanDecision}! This is my personal favorite you have good taste ;)")
        print('')
  elif clanDecision == 'Knight':
        print(f"{name} You are now a {clanDecision}! ...have fun with your boring choice.")   
        print('') 





# name prompt
def nameDrop():
    global hero_name
    hero_name = input('What will your hero name be? ')

    # Update the hero dictionary with the entered name
    hero["name"] = hero_name

    print(f"{hero_name}? Very...original. Moving on -->")
    print("")

# answers = inquirer.prompt(assist)
# clanDecision = answers['characterSelects']
# hero["name"] = answers['hero_name']
# hero["clan"] = clanDecision

# print(f"\nWelcome {hero['name']} of the {hero['clan']} clan!\n")


def leaveOption():
    
        assist = [
        inquirer.List(
          'pubexit',
          message="You walk away. As you exit the pub you bump into someone. It's a wizard!",
          choices=['Apologize', 'Say watch where you going'],
        ),
    ]


        afterleave = inquirer.prompt(assist)['pubexit']

        if afterleave == "Apologize":
            print("You apologize perfusely he instructs you to meet him on the hill @ 4:44 am for your impossible quest.")
            packSupplies()
      

        elif afterleave == f'Say watch where you going':
            print("The wizard turns you into a toad...Game Over")
            ending()
           
            

def pubOptions():
    
        assist = [
        inquirer.List(
          'pubChoose1',
          message="You ask for quest. They laugh in your face. So you...",
          choices=['Cry', 'Leave'],
        ),
    ]

        leave = inquirer.prompt(assist)['pubChoose1']

        if leave == "Cry":
            print("")
            cryOption()
         

        elif leave == "Leave":
            leaveOption()
        


def cryOption():

    global pubOptions
    global pathCorrector


    print("They leave you to wallow in self pity")
    assist = [
        inquirer.List(
          'pubChoose2',
           message=f"The {clanDecision} leaves, dropping a map as they stumble out of the pub.",
          choices=['Happily retrieve it', f'Deliver it back to the {clanDecision}'],
        ),
    ]


    afterb = inquirer.prompt(assist)['pubChoose2']

    if afterb == "Happily retrieve it":
            print("You snatch the map and decide to pack for your impossible quest")
            packSupplies()
      

    elif afterb == f'Deliver it back to the {clanDecision}':
            print("You must be a good person. Pure of heart.")
            print(f"However that gets you nothing in this game. The {clanDecision} snatches it back and shoves you in someone.")
            print("")
            pathCorrector()
            print("")
            packSupplies()
           
           
           


def pathCorrector():
    path3 = 'Its a wizard! You apologize perfusely he instructs you meet him on the hill @ 4:44 am for your impossible quest.'
    print(f'{path3}')




def pubChoice():

    global leave_Option
    global pubOptions
    global cryOption
            
    print(f" As a {clanDecision} in training, You work in the local pub as a busser and you overhear a fellow {clanDecision} speak of a grand adventure no one dare complete.")

    assist = [
        inquirer.List(
          'pubChoose',
          message="What will you do?",
          choices=['Ask for quest', 'continue bussing tables'],
        ),
    ]
  
    pubAction= inquirer.prompt(assist)['pubChoose']
    if pubAction == "Ask for quest":
            print("You ask for quest. They laugh in your face. So you")
            print("")
            pubOptions()
    
    elif pubAction == "continue bussing tables":
        print(f"You punk out and continue being a loser. The {clanDecision} leaves, dropping a map as they stumble out of the pub.")
        print("")
        cryOption()


# ..................................
import inquirer

def packSupplies():

    global pathOption
    assist = [
         inquirer.List(
             'packChoice',
             message="What do you pack? Pick your 2 ",
              choices=['Snacks and your lucky green adventurine stone', 'A sword and a extra pair of underwear'],
            ),
    ]

    while True:
        whatsinyourbag = inquirer.prompt(assist)['packChoice']
        if whatsinyourbag in ['Snacks and your lucky green adventurine stone', 'A sword and a extra pair of underwear']:
            break
        else:
            print("Invalid choice. Please try again.")

    if whatsinyourbag == "Snacks and your lucky green adventurine stone":
        print("Interesting choice, you're either a foodie or a spiritual baddie, either way..I respect it")
        print("")
        print("You set out on your journey..")
        pathOption(whatsinyourbag)
    elif whatsinyourbag == "A sword and a extra pair of underwear":
        print("Interesting choice, you think you'll soil yourself or you just wanted the sword.")
        print("")
        print("You set out on your journey..")
        pathOption(whatsinyourbag)

    # return whatsinyourbag



def pathOption(whatsinyourbag):


    global finalBoss
    global ending
   
   

    print("")
    print("You learn the quest is to reach the top of the mountain of oo. You come to a fork in the road.")
    print("")
    print("On one side you see a dark path with lighting, a rickety bridge, and what appears to be a dragon stalking you.")
    print("")
    print("On the other side you can see light path with colorful skies, fairies fluttering, and what appears to be a easy path to the mountain")
    print("")

    print("")
    print("")
    print("Depending on your items you have chosen will determine if you make it to the mountain for the final boss")
    assist = [
            inquirer.List(
             'pathOptionChoose',
            message="Which path will you take",
            choices=['Dark and dangerous path', 'Light and sparkly path'],
        ),
    ]

    pathChoice = inquirer.prompt(assist)['pathOptionChoose']

    if pathChoice == "Dark and dangerous path" and whatsinyourbag == 'A sword and a extra pair of underwear':
          
             print("")
             print("Sword has no effect on dragon. You wet your pants. Good thing you have an extra pair. Unfortunately you failed. Game Over. ")
             print("Failed! you are like all the ones that came before you, you are exiled from the mountain you shant return for 10 years")
             ending()
             print("")
  

    elif pathChoice == "Light and sparkly path" and whatsinyourbag == 'A sword and a extra pair of underwear':
           
            print("")
            print("This was the right combo, in this story fairys are more dangerous than dragons. Well done. You advance.")
            print("")
            print("As you ascend the mountain you are halted at the sight of a familar face")
            print("")
            finalBoss()
            print("")
       
   
    elif pathChoice == "Dark and dangerous path" and whatsinyourbag == 'Snacks and your lucky green adventurine stone':
      print("")
      print("This was the right combo. The dragon is easily pleased with the snacks. You advance to the mountain")
      print("")
      print("As you ascend the mountain you are halted at the sight of a familar face")
      print("")
      finalBoss()
      print("")

    elif pathChoice == "Light and sparkly path" and whatsinyourbag == 'Snacks and your lucky green adventurine stone': 
      print("")
      print('The fairies are mad and your stone has no effect. You fail, Game over')
      print("Failed! you are like all the ones that came before you, you are exiled from the mountain you shant return for 10 years")
      print("")
      ending()
      print("")


def ending2():
            global ending

            assist = [
             inquirer.List(
             'prizetobe',
               message="This is the end did you expect a prize?",
              choices=['yes', 'no'],
            ),
    ]
  
            whatsinitforme = inquirer.prompt(assist)['prizetobe']
            if whatsinitforme == 'yes':
              print("you are now a slave to the mountain and will serve until another takes ones place")
              print("")
              print("Failed! you are like all the ones that came before you, you are exiled from the mountain you shant return for 10 years") 
              print("")
              ending()
            elif whatsinitforme =='no':
              print('good choice. you win win....now leave and tell your friends to play.')
              print("")
              ending()
              print("")



def riddleAnswer():
    global finalBoss
    global ending2

    while True:
        answerChall = input("What am I?:  ")
        if answerChall.lower() == "river":
            print(f"Well done amazing young {clanDecision}, you have defeated the mountain of oo {name}")
            ending2()
            break
        else: 
            print("Incorrect answer. Please try again.")


# def riddleAnswer():
#     global finalBoss
#     global ending2

#     answerChall= input("What am I?:  ")
#     if answerChall == "river" or "River":
#         print(f"Well done amazing young {clanDecision}, you have defeated the mountain of oo {name}")
#         ending2()
      
#     else: 
#         while answerChall == False:
#             riddleAnswer()


def finalBoss():

  global nameDrop
  global clanDecision
  global riddle 

  print(f" It is you {hero_name}  of the {clanDecision} clan but obviously older. You are confused.")
  print("")
  silence = True
  speak = ["They give you a look", "Silence continues", "A bird poops on you"]
  n = 0
  while silence:
    print (f"{speak[n]}")
    assist = [
      inquirer.List(
          'bossChoice',
          message="Speak first or remain slient?",
          choices=['Say something first', 'Wait'],
        ),
    ]
    answer = inquirer.prompt(assist)['bossChoice']
    if answer == "Wait":
      print (f"Old {hero_name} attacks you!")
      silence = True
      n += 1
      if n == 2:
        n = 0
    elif answer == "Say something first":
      silence = False
      print("'Who are you?'")
      print("'What do you want'")
      print("")
      riddle()
      print("")

 
def Talk():
  global nameDrop
  print(f"{hero_name} is now even more confused ")
  print('')
  

def riddle():

  global finalBoss
  global ending
  global riddleAnswer
  global nameDrop

  print("")
  print(f'After some time, old {hero_name} presents your second challenge')
  print("")

  assist = [
      inquirer.List(
          'riddleChoice',
          message="Do you accept?",
          choices=['Yes', 'No'],
        ),
    ]

  initialBossDecision = inquirer.prompt(assist)['riddleChoice']

  if initialBossDecision == "Yes":
    print("What always runs but never walks.")
    print("Often murmurs, never talks.")
    print("Has a bed but never sleeps.")
    print("An open mouth that never eats")

    print('')
    riddleAnswer()
    print("")

  elif initialBossDecision == "No":
    print("")
    ending()
    print("")

def ending():
            print("")
           

            assist = [
                    inquirer.List(
                     'playAgainChoose',
                message="Would you like to play again? ",
                 choices=['Yes', 'No'],
        ),
    ]

            playAgain = inquirer.prompt(assist)['playAgainChoose']
 
            if playAgain == "No":
                print("Thank you for playing my game! See you next time!")
            else:
                promptIntro()
                quest()
                characterSelect()
                nameDrop()
                pubChoice()
                
                # pathOption()
                # # Talk()
                # finalBoss()
                # ending()






# call all of functions
promptIntro()
quest()
characterSelect()
nameDrop()
pubChoice()



# pathOption()


# finalBoss()
# ending()



