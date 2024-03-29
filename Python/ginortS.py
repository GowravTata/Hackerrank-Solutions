# Enter your code here. Read input from STDIN. Print output to STDOUT

first = input()


def sort_String(s):
    lower_case = []
    upper_case = []
    odd_digits = []
    even_digits = []
    for char in s:
        if char.islower():
            lower_case.append(char)
        elif char.isupper():
            upper_case.append(char)
        elif char.isdigit():
            if int(char) % 2 == 0:
                even_digits.append(char)
            else:
                odd_digits.append(char)
    return (''.join(sorted(lower_case) + sorted(upper_case) + sorted(odd_digits) + sorted(even_digits)))


print(sort_String(first))
