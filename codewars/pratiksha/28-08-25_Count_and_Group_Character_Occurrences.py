"""
<6 kyu> Count and Group Character Occurrences in a String 
https://www.codewars.com/kata/543e8390386034b63b001f31

Write a method that takes a string as an argument and groups the number of time each character appears in the string as a hash sorted by the highest number of occurrences.

The characters should be sorted alphabetically e.g:

get_char_count("cba") == {1: ["a", "b", "c"]}
You should ignore spaces, special characters and count uppercase letters as lowercase ones.

For example:

get_char_count("Mississippi")           ==  {4: ["i", "s"], 2: ["p"], 1: ["m"]}
get_char_count("Hello. Hello? HELLO!")  ==  {6: ["l"], 3: ["e", "h", "o"]}
get_char_count("aaa...bb...c!")         ==  {3: ["a"], 2: ["b"], 1: ["c"]}
get_char_count("abc123")                ==  {1: ["1", "2", "3", "a", "b", "c"]}
get_char_count("aaabbbccc")             ==  {3: ["a", "b", "c"]}
"""
#Solution
def get_char_count(strng: str) -> dict[int, list[str]]:
    valid_chars = ""
    for char in strng:
        if char.isalnum():
            valid_chars += char.lower()

    #count each characters frequency      
    count_char = {}
    for char in valid_chars:
        if char in count_char:
            count_char[char] += 1
        else:
            count_char[char] = 1

    #group by frequency
    group_char = {}
    for char, freq in count_char.items():
        if freq not in group_char:
            group_char[freq] = []
        group_char[freq].append(char)

    #sorting
    for freq in group_char:
        group_char[freq].sort()

    sorted_count = {}
    for freq in sorted(group_char.keys(), reverse=True):
        sorted_count[freq] = group_char[freq]

    return sorted_count


#Function call
result = get_char_count("Mississippi")  
print(result)
result = get_char_count("Hello. Hello? HELLO!")  
print(result)
result = get_char_count("aaa...bb...c!")  
print(result)
result = get_char_count("abc123")  
print(result)
result = get_char_count("aaabbbccc")  
print(result)

#Output
"""
{4: ['i', 's'], 2: ['p'], 1: ['m']}
{6: ['l'], 3: ['e', 'h', 'o']}     
{3: ['a'], 2: ['b'], 1: ['c']}     
{1: ['1', '2', '3', 'a', 'b', 'c']}
{3: ['a', 'b', 'c']}

"""