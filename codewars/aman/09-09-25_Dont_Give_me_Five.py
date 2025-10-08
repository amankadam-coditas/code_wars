"""
Question Link : https://www.codewars.com/kata/5813d19765d81c592200001a/train/python
<| 7 kyu |> | 09th Sept '25
Don't give me five!
In this kata you get the start number and the end number of a region and should return the count of all numbers except numbers with a 5 in it. The start and the end number are both inclusive!

Examples:

1,9 -> 1,2,3,4,6,7,8,9 -> Result 8
4,17 -> 4,6,7,8,9,10,11,12,13,14,16,17 -> Result 12
"""

# Solution
def dont_give_me_five(start,end):
    res = []
    for i in range(start, end+1):
        if "5" not in str(i) :
            res.append(i)
    return len(res) 

# Input / Output
# OUTPUT | Expected : 12
dont_give_me_five(4, 17)

# Actual Ouput
# >> 12