while True:
    player1 = str(input("player1 (Rock, Paper, Scissors): "))
    player2 = str(input("player2 (Rock, Paper, Scissors): "))

    if (player1 == "Rock" and player2 == "Scissors") | (player1 == "Scissors" and player2 == "paper") | (player1 == "Paper" and player2 == "Rock"):
        print("player1 wins!!")
    elif (player2 == "Rock" and player1 == "Scissors") | (player2 == "Scissors" and player1 == "paper") | (player2 == "Paper" and player1 == "Rock"):
        print("player2 wins!!")
    else:
        print("It is a tie, please play again")
        continue
    if input("Do you want to leave the game(Y/N)?") == "Y":
        break


