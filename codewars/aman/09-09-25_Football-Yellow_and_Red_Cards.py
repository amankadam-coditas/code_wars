"""
Question Link : http://codewars.com/kata/5cde4e3f52910d00130dc92c/train/python
<| 6 kyu |> | 09th Sept '25
Most football fans love it for the goals and excitement. Well, this Kata doesn't. You are to handle the referee's little notebook and count the players who were sent off for fouls and misbehavior.

The rules: Two teams, named "A" and "B" have 11 players each; players on each team are numbered from 1 to 11. Any player may be sent off the field by being given a red card. A player can also receive a yellow warning card, which is fine, but if he receives another yellow card, he is sent off immediately (no need for a red card in that case). If one of the teams has less than 7 players remaining, the game is stopped immediately by the referee, and the team with less than 7 players loses.

A card is a string with the team's letter ('A' or 'B'), player's number, and card's color ('Y' or 'R') - all concatenated and capitalized. e.g the card 'B7Y' means player #7 from team B received a yellow card.

The task: Given a list of cards (could be empty), return the number of remaining players on each team at the end of the game (as a tuple of 2 integers, team "A" first). If the game was terminated by the referee for insufficient number of players, you are to stop the game immediately, and ignore any further possible cards.

Note for the random tests: If a player that has already been sent off receives another card - ignore it.
"""

# Solution
def men_still_standing(cards):
    # Both Team 11 Players
    a = b = 11
    y_color = {}
    r_color = set()

    # Helper function to eliminate players from team as per card color (fouls)
    def remove_player(team):
        nonlocal a, b
        if team == "A":
            a -= 1
        else:
            b -= 1

    for card in cards:
        if any([a < 7, b < 7]):
            return a,b
        
        team = card[0]
        card_color = card[-1]
        player = card[0:-1]

        if card_color == "Y":

            if player in r_color:
                continue 

            if player in y_color:
                if y_color[player]["removed"]:
                    continue

                y_color[player]["count"] += 1

                if y_color[player]["count"] >=2:
                    y_color[player]["removed"] = True
                    remove_player(team)
            else :
                y_color[player] = {"count":1, "removed": False}

        elif player not in r_color:

            if player in y_color and y_color[player]["removed"]:
                continue
            remove_player(team)

            r_color.add(player)

    return a, b


# Input / Output | expected (9,9)

res = men_still_standing(['B9R', 'A2Y', 'B8Y', 'A2Y', 'A6R', 'A1Y', 'A2R',
                           'B4Y', 'B1Y', 'B8R', 'A6Y', 'A5Y', 'B11Y', 'B9R',
                             'B9Y', 'A8Y']
)
print(res)

# OUTPUT
# >> (9, 9)

# Input / Output | expected (9,10)

res1 = men_still_standing(["A4Y", "A5R", "B5R", "A4Y", "B6Y"])

print(res1)

# OUTPUT
# >> (9, 10)

"""
CodeWars Submitted Solution Link : 
https://www.codewars.com/kata/reviews/5ce007bc802fe800012d7edd/groups/68c09d7229a4b1135cb9027c
"""