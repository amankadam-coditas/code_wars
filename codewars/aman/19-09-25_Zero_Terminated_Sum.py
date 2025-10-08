"""
Zero Terminated Sum
Question Link : https://www.codewars.com/kata/5a2d70a6f28b821ab4000004/train/python
<| 7 kyu |> | 19th Sept '25
You have managed to intercept an important message and you are trying to read it.

You realise that the message has been encoded and can be decoded by switching each letter with a corresponding letter.

You also notice that each letter is paired with the letter that it coincides with when the alphabet is reversed.

For example: "a" is encoded with "z", "b" with "y", "c" with "x", etc

You read the first sentence:

"r slkv mlylwb wvxlwvh gsrh nvhhztv"
After a few minutes you manage to decode it:

"i hope nobody decodes this message"
Create a function that will instantly decode any of these messages

You can assume no punctuation or capitals, only lower case letters, but remember spaces!
"""

# Solution
def find_sum(s):
    count = 0
    for i in s:
        count += int(i)
    return count

def largest_sum(s):
    print(s)
    arr = s.strip("0").split("0")
    sum_arr = [find_sum(i) for i in arr if i != "" ]
    if len(sum_arr) > 0 :
        return max(sum_arr)
    return 0

# Input
>> largest_sum("72102450111111090")

# Output
>> 11

# Input
>> largest_sum("123004560")

# Output
>> 15