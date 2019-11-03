# points_allocated_for_each_player
import random

points1 = 0
points2 = 0


def hand_cricket(iterate, no_of_rounds):
    terms = ['rock', 'paper', 'pencil', 'scissor']
    first_player = input("First_Player, Enter the term: ")
    second_player = random.choice(terms)
    print("The computer's term is: {}".format(second_player))

    # if terms.__contains__(first_player) and terms.__contains__(second_player):
    if first_player in terms and second_player in terms:
        # defining the variables as global for single time initialisation
        global points1, points2
        # creating a list using the inputs
        lists = [first_player, second_player]
        lists.sort()
        # print(lists)
        # concatenating the inputs in the list
        word = lists[0] + '+' + lists[1]
        # print(word)
        # creating a dictionary using all the combinations and the results
        players = {
            'rock+scissor': 'rock',
            'paper+rock': 'paper',
            'pencil+rock': 'rock',
            'paper+pencil': 'pencil',
            'paper+scissor': 'scissor',
            'pencil+scissor': 'scissor',
            'paper+paper': 'none',
            'pencil+pencil': 'none',
            'rock+rock': 'none'}
        # the result of the combination provided is retrieved
        result = players[word]
        # print(result)
        # based on the result the points are incremented
        if result == first_player:
            points1 = points1 + 1
        elif result == second_player:
            points2 = points2 + 1
        else:
            points1 = points1 + 0
            points2 = points2 + 0

        print("First Player Points: {}".format(points1))
        print("Second Player Points: {}".format(points2))
        # at the last iteration the result is being displayed
        if iterate == no_of_rounds:
            if points1 > points2:
                print("First Player Wins!!!")
            else:
                print("Second Player Wins!!!")

    else:
        print("Enter the correct term.")


print("Rock Paper Pencil Scissor!!!")
print("Let's start the game")
no_of_rounds = int(input("Enter the number of rounds to be played: "))

for i in range(1, no_of_rounds):
    print("{} round!!".format(i))
    hand_cricket(i, no_of_rounds)
