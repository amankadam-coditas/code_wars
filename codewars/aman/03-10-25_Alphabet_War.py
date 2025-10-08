"""
Question Link : https://www.codewars.com/kata/5938f5b606c3033f4700015a/train/python
<| 6 kyu |> | 03rd Oct '25
Alphabet war - airstrike - letters massacre

Introduction
There is a war...between alphabets!
There are two groups of hostile letters. The tension between left side letters and right side letters was too high and the war began. The letters called airstrike to help them in war - dashes and dots are spread throughout the battlefield. Who will win?

Task
Write a function that accepts a fight string which consists of only small letters and * which represents a bomb drop place. Return who wins the fight after bombs are exploded. When the left side wins return Left side wins!, and when the right side wins return Right side wins!. In other cases, return Let's fight again!.

The left side letters and their power:

 w - 4
 p - 3 
 b - 2
 s - 1
The right side letters and their power:

 m - 4
 q - 3 
 d - 2
 z - 1
The other letters don't have power and are only victims.
The * bombs kill the adjacent letters ( i.e. aa*aa => a___a, **aa** => ______ );

Example (Input --> Output)
"s*zz"           --> "Right side wins!"
"*zd*qm*wp*bs*"  --> "Let's fight again!"
"zzzz*s*"        --> "Right side wins!"
"www*www****z"   --> "Left side wins!"
"""

# Solution
def alphabet_war(fight):
    team_left = {"w":4, "p":3, "b":2, "s":1}
    team_right = {"m":4, "q":3, "d":2, "z":1}
    left = right = 0
    destroyed = set()
    for k, v in enumerate(fight):
        if v == "*":
            if k > 0:
                destroyed.add(k-1)
            if k < len(fight)-1:
                destroyed.add(k+1)
                
    for index, char in enumerate(fight):
        if index in destroyed:
            continue
        if char in team_left:
            left += team_left[char]
        if char in team_right:
            right += team_right[char]
    if left > right:
        return "Left side wins!"
    if right > left:
        return "Right side wins!"
    return "Let's fight again!"

# -Solution END-

# INPUT
>>> alphabet_war("z*dq*mw*pb*s")

# OUTPUT
>>> "Let's fight again!"

# INPUT
>>> alphabet_war("zz*zzs")

# OUTPUT
>>> "Right side wins!"