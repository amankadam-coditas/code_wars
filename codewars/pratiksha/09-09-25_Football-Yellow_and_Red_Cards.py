"""
<6 kyu> Football - Yellow and Red Cards
https://www.codewars.com/kata/5cde4e3f52910d00130dc92c/python

Most football fans love it for the goals and excitement. Well, this Kata doesn't. You are to handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.

The rules: Two teams, named "A" and "B" have 11 players each; players on each team are numbered from 1 to 11. Any player may be sent off the field by being given a red card. A player can also receive a yellow warning card, which is fine, but if he receives another yellow card, he is sent off immediately (no need for a red card in that case). If one of the teams has less than 7 players remaining, the game is stopped immediately by the referee, and the team with less than 7 players loses.

A card is a string with the team's letter ('A' or 'B'), player's number, and card's color ('Y' or 'R') - all concatenated and capitalized. e.g the card 'B7Y' means player #7 from team B received a yellow card.

The task: Given a list of cards (could be empty), return the number of remaining players on each team at the end of the game (as a tuple of 2 integers, team "A" first). If the game was terminated by the referee for insufficient number of players, you are to stop the game immediately, and ignore any further possible cards.

Note for the random tests: If a player that has already been sent off receives another card - ignore it.
"""
#Solution
def men_still_standing(cards):
    team_A = 11
    team_B = 11

    yellow_A = {}  # {player_no : count_of_yellow}
    yellow_B = {}

    sent_off_A = []  # list of player_no sent off
    sent_off_B = []

    for card in cards:
        team = card[0]
        player = int(card[1:-1])
        color = card[-1]

        #Skip players already sent off
        if team == 'A' and player in sent_off_A:
            continue
        if team == 'B' and player in sent_off_B:
            continue

        if color == 'Y':
            if team == 'A':
                #Check if player is in yellow_A else yellow_B
                if player in yellow_A:
                    yellow_A[player] += 1
                else:
                    yellow_A[player] = 1

                #If player now has 2 yellow cards, send off
                if yellow_A[player] == 2:
                    sent_off_A.append(player)
                    team_A -= 1
            else:
                if player in yellow_B:
                    yellow_B[player] += 1
                else:
                    yellow_B[player] = 1

                if yellow_B[player] == 2:
                    sent_off_B.append(player)
                    team_B -= 1

        elif color == 'R':
            if team == 'A':
                sent_off_A.append(player)
                team_A -= 1
            else:
                sent_off_B.append(player)
                team_B -= 1

        #Terminate if players < 7
        if team_A < 7 or team_B < 7:
            break

    return (team_A, team_B)



#Function Call
result = men_still_standing(["A4Y", "A5R", "B5R", "A4Y", "B6Y"])
print(result)

result = men_still_standing(["A4R", "A6R", "A8R", "A10R", "A11R"])
print(result)


#Output
"""
(9, 10)
(6, 11)

"""