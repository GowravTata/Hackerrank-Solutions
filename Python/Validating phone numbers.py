# Enter your code here. Read input from STDIN. Print output to STDOUT
import re


def check_num(x):
    if re.search(r'^[789]\d{9}$', x):
        return 'YES'
    return 'NO'


N = int(input())
for _ in range(N):
    i = input()
    print(check_num(i))
