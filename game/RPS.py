import random 

def RPS(): 
    
    computer_score = 0
    player_score = 0

    options = ["stone", "paper", "scissors"]

    for i in range(5):

        result = ""
        computer_choice = random.choice(options)

        print("choices: ", options)

        player_choice = input("Enter a choice :").lower()

        if player_choice not in options:
                print("Invalid choice")
        elif(player_choice == computer_choice):
                print("It's a tie!")
                print("computer choice:", computer_choice)
        elif(player_choice == "stone" and computer_choice == "scissors" or player_choice == "paper" and computer_choice == "stone" or player_choice == "scissors" and computer_choice == "paper"):
                result = "Victory!"
                print(result)
                print("computer choice:", computer_choice)
        else:
                result = "Defeat :("
                print(result)
                print("computer choice:", computer_choice)

        if  result == "Victory!" :
                player_score += 1
                print("player score; ",player_score)
        elif result == "Defeat :(" :
                computer_score += 1
                print("computer score: ",computer_score)
        
        if player_score == 3:
               print("Final Winner : Player ")
               break
        elif computer_score == 3:
                print("Final Winner : Computer ")
                break       
                      
RPS() 