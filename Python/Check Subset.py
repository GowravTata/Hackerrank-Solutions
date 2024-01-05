# Enter your code here. Read input from STDIN. Print output to STDOUT
first = int(input())

all_values = [input() for i in range(first * 4)]

i = 1
while i <= first * 4:
    first_set = set(map(int, all_values[i].split()))
    second_set = set(map(int, all_values[i + 2].split()))
    print(first_set.issubset(second_set))
    i += 4
