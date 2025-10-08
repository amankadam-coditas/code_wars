"""
Question Link : https://www.codewars.com/kata/57b5907920b104772c00002a/train/python
<| 7 kyu |> | 02th Sept '25
The Cat In The Hat has cat A under his hat, cat A has cat B under his hat and so on until Z

The Cat In The Hat is 2,000,000 cat units tall.

Each cat is 2.5 times bigger than the cat underneath their hat.

Find the total height of the cats if they are standing on top of one another.

Counting starts from the Cat In The Hat

n = the number of cats

fix to 3 decimal places.
"""

# Solution
def height(n):
    # The Cat In The Hat is 2,000,000 cat units tall.
    cat_unit = 2000000
    total_height = cat_unit
    
    for i in range(n, 0, -1):
        res = cat_unit / 2.5
        total_height += res
        cat_unit =  res
    
    # fixing the output to 3 decimals
    return f"{total_height:.3f}"