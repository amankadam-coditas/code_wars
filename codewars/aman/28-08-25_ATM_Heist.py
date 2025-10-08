"""
Question Link: https://www.codewars.com/kata/543e8390386034b63b001f31/train/python
<| 6 kyu |> | 28th Aug '25

Your function should return this maximum possible thrill value.

For example, if we have four ATMs: [2, 3, 4, 5], the ATM at index 0 will
transfer a dollar to index 1, $2 to index 2, and $3 to index 3. Similarly, 
the ATM at index 2 will transfer $1 to indexes 1 and 3, and $2 to index 0.

Note that in the case above, Beyonce will either steal from the last ATM (index 3) 
twice, or steal from index 0 and index 3, because it nets her the maximum value of 
10 ($5 + $5 + $0 transfer vs. $2 + $5 + $3 transfer). Either way, the answer is 10, 
returned as an integer.

Examples:

atms = [2,3,4,5]
maximum_thrill(atms) => 10 # $5 + $5 + $0 transferred (atms[3] and atms[3] again)

atms = [10, 10, 11, 13, 7, 8, 9]
maximum_thrill(atms) => 26 # $10 + $13 + $3 transfer between each (atms[0] and atms[3])

atms = [2, 3, 4, 5, 10, 6, 7, 8, 9, 10, 11, 12, 4, 4, 2, 2, 12, 8]
maximum_thrill(atms) => 34  # $10 + $12 + $12 transfer between each (atms[4] and atms[16])

Your solution must be O(n) to pass!
"""

# Solution
def maximum_thrill(atms):
    if not atms:
        return 0

    m_minus = float("-inf")
    m_plus = float("-inf")
    m_same = float("-inf")
    
    for i, v in enumerate(atms):
        m_minus = max(m_minus, v-i)
        m_plus = max(m_plus, v+i)
        m_same = max(m_same, 2*v)
    
    t1 = m_minus + max(v + i for i, v in enumerate(atms))
    t2 = m_plus + max(v - i for i, v in enumerate(atms))
    return max(t1, t2, m_same)