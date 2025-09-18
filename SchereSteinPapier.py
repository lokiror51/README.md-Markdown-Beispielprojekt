import random

list = ['schere', 'stein', 'papier']
player_score = 0

while True:
    computer_choice = random.choice(list)

    players_choice = input("Wählen Sie Schere, Stein oder Papier\n").lower()

    if players_choice.lower() not in list:
        print("Ungültige Eingabe")
    else:
        if players_choice == computer_choice:
            print("Tie")
        elif list.index(players_choice) == 0 and list.index(computer_choice) == 2:
            print("You've won!")
            player_score += 1
        elif list.index(computer_choice) == 0 and list.index(players_choice) == 2:
            print("You've lost!")
            player_score -= 1
        elif list.index(players_choice) > list.index(computer_choice):
            print("You've won!")
            player_score += 1
        else:
            print("You've lost")
            player_score -= 1
        
        print(f"Computer chose: {computer_choice}")
        print(f"\nYour Score: {player_score} \n")