"""
Question Link : https://www.codewars.com/kata/5a0efbb7c374cb69970000cf/train/javascript
<| 7 kyu |> | 23th Sept '25

Reverse a message so that the words and 
letters passed into it are made lower 
case and reversed. In addition, capitalise 
the first letter of the newly reversed words. 
If a number or symbol(!#,>) is now in the first 
position of the word, no capitalisation needs 
to occur.

Example:

reverseMessage('This is an example of a Reversed Message!');
Returns: '!egassem Desrever A Fo Elpmaxe Na Si Siht'
"""

# Solution
def reverseMessage(input : str):
    sentence = input.split(" ")
    res = []
    for i in range(len(sentence)-1, -1, -1):
        res.append(sentence[i][::-1].capitalize())
    return " ".join(res)


# Input :
>> reverseMessage('Hello there')

# Output :
>> 'Ereht Olleh'