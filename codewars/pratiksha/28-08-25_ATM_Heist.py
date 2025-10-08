"""
<6 kyu> ATM Heist
https://www.codewars.com/kata/5d8108a41e94580023bd6419

Full credit to dramforever for coming up with an O(n) solution to this problem!
Beyonce (no relation to Beyoncé) is planning a heist at a local casino. She wants steal the money from two ATMs.
While she mostly cares about getting away with money, she's also interested in a unique fact about the ATMs at this particular casino; 
once a day, each ATM transfers one dollar to each other machine for each unit of distance away it is (e.g. in [0,1] both indices are 1 unit apart).

(Additionally, when emptied, each ATM will automatically refill with the exact same dollar amount as before, 
so it's possible to steal from the same ATM twice.)

Because she gets a thrill out of the fact that so much money has been transferred between ATMs, 
what she's ultimately interested in is stealing from the two ATMs which have the highest combined total money inside, 
plus number of dollars each transferred to the other.

Your function should return this maximum possible thrill value.

For example, if we have four ATMs: [2, 3, 4, 5], the ATM at index 0 will transfer a dollar to index 1, $2 to index 2, and $3 to index 3. 
Similarly, the ATM at index 2 will transfer $1 to indexes 1 and 3, and $2 to index 0.

Note that in the case above, Beyonce will either steal from the last ATM (index 3) twice, or steal from index 0 and index 3,
because it nets her the maximum value of 10 ($5 + $5 + $0 transfer vs. $2 + $5 + $3 transfer). 
Either way, the answer is 10, returned as an integer.

Examples:

atms = [2,3,4,5]
maximum_thrill(atms) => 10 # $5 + $5 + $0 transferred (atms[3] and atms[3] again)

atms = [10, 10, 11, 13, 7, 8, 9]
maximum_thrill(atms) => 26 # $10 + $13 + $3 transfer between each (atms[0] and atms[3])

atms = [2, 3, 4, 5, 10, 6, 7, 8, 9, 10, 11, 12, 4, 4, 2, 2, 12, 8]
maximum_thrill(atms) => 34  # $10 + $12 + $12 transfer between each (atms[4] and atms[16])
Note: These are magic ATMs, so don't worry about accounting for whether an ATM has enough money to transfer.

Your solution must be O(n) to pass!
"""
#atms[i] + atms[j] is the money you get from both ATMs
#abs(i - j) is the amount each ATM transferred to the other

#Solution
def maximum_thrill(atms): 
    n = len(atms)
    max_thrill = 0

    for i in range(n):
        for j in range(i, n):  
            thrill = atms[i] + atms[j] + abs(i - j)
            if thrill > max_thrill:
                max_thrill = thrill

    return max_thrill

#Function call
atms = [2,3,4,5]
result = maximum_thrill(atms) 
print(result)
atms = [10, 10, 11, 13, 7, 8, 9]
result = maximum_thrill(atms) 
print(result)
atms = [2, 3, 4, 5, 10, 6, 7, 8, 9, 10, 11, 12, 4, 4, 2, 2, 12, 8]
result = maximum_thrill(atms) 
print(result)


#Output
"""
10
26
34

"""


