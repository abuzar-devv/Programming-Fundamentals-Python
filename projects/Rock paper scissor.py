#Need to add features yet (loops , visualization)

print("Welcome to rock , paper and scissor game!")

player_1=input("Enter (Rock , Paper or scissor) :").lower()
player_2=input("Enter (Rock , Paper or scissor) :").lower()

moves=("rock","paper","scissor")


if (player_1 in moves) and (player_2 in moves):

    if (player_1=="rock" and player_2=="paper"):
        print("Player 2 wins!")

    elif (player_1=="rock" and player_2=="scissor"):
        print("player 1 wins!")

    elif (player_1=="paper" and player_2=="rock"):
        print("Player 1 wins!")

    elif (player_1=="paper" and player_2=="scissor"):
        print("Player 2 wins!")

    elif (player_1=="scissor" and player_2=="rock"):
        print("player 2 wins!")

    elif (player_1=="paper" and player_2=="paper"):
        print("Tie!")

    elif (player_1=="scissor" and player_2=="scissor"):
        print("Tie")

    elif (player_1=="rock" and player_2=="rock"):
        print("Tie")

    elif (player_1=="scissor" and player_2=="paper"):
        print("Player 1 wins!")

    else:
        print("Invalid!")

else:
    print("Enter valid moves only (rock , paper or scissor) :")

