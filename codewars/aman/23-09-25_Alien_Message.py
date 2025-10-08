"""
Message from Aliens
Question Link : https://www.codewars.com/kata/598980a41e55117d93000015/train/python
<| 6 kyu |> | 23rd Sept '25
Task
Aliens send messages to our planet, but they use a very strange language. 
Try to decode the messages!

Category : Puzzles | Fundamentals
"""

alien_map = {
    "|)": "d",
    "|": "i",
    "[-": "e",
    "_\\~": "s",
    "|_|": "u",
    "()_": "q",
    "()": "o",
    "|^": "p",
    "]3": "b",
    "(": "c",
    "><": "x",
    "/<": "k",
    "`/": "y",
    "/?": "r",
    "~|~": "t",
    "|_": "l",
    "|-|": "h",
    "/=": "f",
    "|\\|": "n",
    "/\\": "a",
    "\\/\\/": "w",
    "(_,": "g",
    "~/_": "z",
    "_T": "j",
    "|\\/|": "m",
    "\\/": "v",
}

# Solution
def decode(text):
    split_sentence = text.split("__")
    res = []
    split_char = text[0]
    for i in range(len(split_sentence) - 1, -1, -1):
        word = ""
        for char in split_sentence[i].split(split_char):
            if char != "":
                val = alien_map.get(char)
                if val:
                    word += val
        res.append(word[::-1])
    return " ".join(res)

# Input
>> decode('..[-.|_.|^....().[-.|^.__..|)...|.|^.|_|..~|~._\\~.__...[-..|.|)..')

# Output
>> 'die stupid people'

# Input
>> decode('}/\\}~|~}/\\}/<}__}|)}}}[-}~|~}/\\}(}|}|_}|^}|_|}|)}__}|)}}}|\\|}|}/=}__}()}}}~|~}__}`/}/?}}~|~}')

# Output
>> 'try to find duplicated kata'
