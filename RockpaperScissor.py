import random
choices=["Rock","Paper","Scissor"]
while True:
    user_choice=input("Enter your choice ")
    if user_choice not in choices:
        print("enter valid choice like Rock Paper Scissor")
        continue
    bot_choice=random.choice(choices)
    print("computer select a ",bot_choice)
    if user_choice==bot_choice:
        print("Tie")
    elif (user_choice == "rock" and bot_choice == "scissors") or  (user_choice == "paper" and bot_choice == "rock") or (user_choice == "scissors" and bot_choice == "paper"):
        print("You win")
    else:
        print("Yos lost")    
    contn=input("You want to continue [y/n] >")
    if contn=='n':
        break         
    
    