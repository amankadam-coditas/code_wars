"""
<7 kyu>  Cats in hats
https://www.codewars.com/kata/57b5907920b104772c00002a

The Cat In The Hat has cat A under his hat, cat A has cat B under his hat and so on until Z
The Cat In The Hat is 2,000,000 cat units tall.
Each cat is 2.5 times bigger than the cat underneath their hat.
Find the total height of the cats if they are standing on top of one another.
Counting starts from the Cat In The Hat
n = the number of cats

fix to 3 decimal places.
"""
#Solution
def height(n):
    total = 2000000  #Cat in Hat
    cat_height = 2000000

    for _ in range(n):
        cat_height /= 2.5
        total += cat_height

    return f"{total:.3f}"


#Function call
total = height(7)
print(total)

total = height(0)
print(total)


#Output
"""
3331148.800
2000000.000

"""