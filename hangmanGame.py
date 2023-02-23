import random
name = input("Enter your name : " )
print("Welcome to Hangman Game,",name)
restart = "yes"

def hangman():
    x = ""
    s = {"sports" : ("cricket","football","badminton","volleyball","hockey") , "animals" : ("tiger","panda","rabbit","cheetah","leopard","crocodile") , "birds" : ("eagle","woodpecker","hummingbird","vulture","parrot","peacock") , "fruits" : ("apple","orange","banana","watermelon","jackfruit") ,"musical instruments" : ("keyboard","guitar","clapbox","flute","violin","trumpet")}
    genre_list = list(s.keys())
    x = input('''Choose the genre:
    Sports     Animals     Birds     Fruits   Musical instruments
    ''').lower()
    item_list = list(s[x])
    command = input(f"Are you ready, {name} ? ").lower()
    print("You have total five lives.")
    while command != "no":
        def hangman_tries():
            stages = ['''
             --------
             |      |
             |
             |
             |
             |
             -
          ''',
          '''
             --------
             |      |
             |      0
             |
             |
             |
             -
          ''',
          '''
             --------
             |      |
             |      0
             |      |
             |      |
             |
             -
          ''',
          '''
             --------
             |      |
             |      0
             |     /|
             |      |
             |
             -
          ''',
          '''
             --------
             |      |
             |      0
             |     /|\\
             |      |
             |
             -
          ''',
          '''
             --------
             |      |
             |      0
             |     /|\\ 
             |      |
             |     / 
             -
          ''',
          '''
             --------
             |      |
             |      0
             |     /|\\ 
             |      |
             |     / \\
             -
          ''']
            
            if count == 0:
                print("5 lives left.")
                print(stages[0],"\n")
            if count == 1:
                print("4 lives left.")
                print(stages[1],"\n")
            if count == 2:
                print("3 lives left.")
                print(stages[2],"\n")
            if count == 3:
                print("2 lives left.")
                print(stages[3],"\n")
            if count == 4:
                print("1 lives left. BE CAREFUL !!!")
                print(stages[4],"\n")
            if count == 5:
                print(stages[5])
            
        choice = random.choice(item_list)
        print("The word  contains",len(choice),"letters.")
        print("_ " * len(choice))
        guess = input("Enter your guess : ")
        s1,s2 = "",""
        guessed = set()
        count = 0
        flag = False
        item_list.remove(choice)
        while guess != None:
            if guess in guessed:
                flag = True
            if guess not in guessed and guess in choice:
                print("Your guess is in the word.")
            if guess not in choice:
                print("Sorry! Your guess is wrong.")
            guessed.add(guess)
            for (i,elem) in enumerate(choice):
                if elem in guessed:
                    s1 += elem + " "
                    s2 += elem
                else:
                    s1 += "_ "
            print(s1)
            if flag == True:
                print("You have already guessed the letter.")

            if guess in choice:
                count += 0
            else:
                if flag == True:
                    count += 0
                else:    
                    count += 1
            flag = False
            if s2 == choice:
                print("YOU WON!!!",name,"\n")
                break
            if count == 5:
                print("GAME OVER!",name,"\n")
                print("The answer is",choice)
                break
            hangman_tries()
            s1 = ""
            s2 = ""
            print("You have already guessed these letters,",guessed)
            
            guess = input("Enter your guess : ")

        if len(item_list) == 0:
            print("CONGRATS! YOU HAVE SUCCESSFULLY FOUND OUT ALL THE WORDS IN THE GENRE.")
            restart = input("Do you want to play any other genre ? ").lower()
            if restart == "yes":
                hangman()
            elif restart == "no":
                print("BYE !!!",name)
                break
            else:
                restart = input("Sorry! I cannot understand. Do you want to play any other genre ? ")
        else:        
            command = input("Do you wish to continue ? ").lower()
            if command == "no":
                break
hangman()
print("BYE!!!",name)
        
    
    
    
    
