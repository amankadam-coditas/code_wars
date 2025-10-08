"""
Question Link: https://www.codewars.com/kata/543e8390386034b63b001f31/train/python
<| 6 kyu |> | 28th Aug '25
Title : Count and Group Character Occurrences in a String
Write a method that takes a string as an argument and groups
the number of time each character appears in the string as a 
hash sorted by the highest number of occurrences.

`
get_char_count("cba") == {1: ["a", "b", "c"]}
`

The characters should be sorted alphabetically e.g:
For example:
`
get_char_count("Mississippi")           ==  {4: ["i", "s"], 2: ["p"], 1: ["m"]}
get_char_count("Hello. Hello? HELLO!")  ==  {6: ["l"], 3: ["e", "h", "o"]}
get_char_count("aaa...bb...c!")         ==  {3: ["a"], 2: ["b"], 1: ["c"]}
get_char_count("abc123")                ==  {1: ["1", "2", "3", "a", "b", "c"]}
get_char_count("aaabbbccc")             ==  {3: ["a", "b", "c"]}
`
"""
# Solution:

def get_char_count(strng: str) -> dict[int, list[str]]:
    store = ""
    dic = {}
    res = {}
    final_res = {}
    for char in strng.replace(" ","").lower():
        if char in store:
            if char in dic:
                dic[char]+=1
        else:
            store += char
            if char.isalnum():
                dic[char] = 1
    
    for key,value in dic.items():
        if value in res:
            res[value].append(key)
        else:
            res[value] = [key]
            
    for i in res:
        final_res[i] = sorted(res[i])

    return final_res