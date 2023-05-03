import random
from words import words


print("|-| /-\ |\| [+ |\/| /-\ |\|")
print("=================================================================")
print("||You will have 6 lives. 1 wrong guess  = 1 life lost||")
print(" ")

while True:

    pick=random.choice(words)
    picked=pick.lower()
    
    tries=1
    wrong_guess=" "
    blank="_"*len(picked)
    pick_list=list(picked)
    blank_list=list(blank)
    
    print("================================================================")
    play=input("Are you ready to play Hangman? ")
    
    
    if play=="yes":
        print("Number of letters = ",len(picked))
        print(" ")
        print(blank)
        print("Hint: Its a verb")

        
        while blank_list!=pick_list:
            print("========================================================")
            guess=input("Guess a letter: ")
            print(" ")

            if guess in picked:

                i=0
                while i<=len(picked)-1:
                    if guess==pick_list[i]:
                        print("That's right.")
                        blank_list[i]=guess
                    i=i+1
                blank_final=' '
                for x in blank_list:
                    blank_final=blank_final+x
                print(blank_final)

                
                
            else:
                print(f"{guess} IS NOT there.")
                
                wrong_guess=wrong_guess+guess
                print("Wrong guesses:",wrong_guess)
                if tries==1:
                    print('''
|------|
|      O
|     
|      
|     
''')
                elif tries==2:
                    print('''
|------|
|      O
|      |
|      |
|  
''')
                elif tries==3:
                    print('''
|------|
|      O
|     /|
|      |
|
''')
                elif tries==4:
                    print('''
|------|
|      O
|     /|\x5c
|      |
|
''')
                elif tries==5:
                    print('''
|------|
|      O
|     /|\x5c
|      | 
|     / 
''')
                elif tries==6:
                    print('''
|------|
|      O
|     /|\x5c
|      |
|     / \x5c
''')
                    print("You lost.")
                    print("The word was ",pick)
                    break;
                tries=tries+1
        if blank_list==pick_list:
            print("Congratulations ! You won.")
            
              
    else:
        break;
