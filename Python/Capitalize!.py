
import string
# Complete the solve function below.
def solve(s):
    for letter in s.split():
        if not letter[0].isdigit():
            s= s.replace(letter,letter.title())
    return s
