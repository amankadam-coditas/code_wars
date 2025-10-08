"""
Question Link : https://www.codewars.com/kata/5fc7d2d2682ff3000e1a3fbc/train/python
<| 6 kyu |> | 23th Sept '25

In this kata, you have an input string and you 
should check whether it is a valid message. To 
decide that, you need to split the string by the 
numbers, and then compare the numbers with the number 
of characters in the following substring.

For example "3hey5hello2hi" should be split into 3, 
hey, 5, hello, 2, hi and the function should return true, 
because "hey" is 3 characters, "hello" is 5, and "hi" is 
2; as the numbers and the character counts match, the result 
is true.

Notes:

Messages are composed of only letters and digits
Numbers may have multiple digits: e.g. "4code13hellocodewars" is a valid message
Every number must match the number of character in the following substring, otherwise the message is invalid: e.g. "hello5" and "2hi2" are invalid
If the message is an empty string, you should return true
"""

# Solution
def is_a_valid_message(message):
    num_list = []
    num_track = ""
    char_list = [] 
    char_track = ""  
    for char in message:
        if char.isnumeric():
            num_track+=char
            if char_track:
                char_list.append(char_track)
                char_track = ""
        else:
            char_track+=char
            if num_track:
                num_list.append(int(num_track))
                num_track = ""
    char_list.append(char_track)
    return num_list == list(map(len,char_list))

# Input
>> is_a_valid_message("1a2bb3ccc4dddd5eeeee")

# Output
>> True

# Input
>> is_a_valid_message("17HIYNWINZXCJZJJZEJEPKZCPL141910IOFNOOJURMDTTWIGCHE7JJSBLMAWDZTSDPCAONKZPKDC")

# Output
>> False