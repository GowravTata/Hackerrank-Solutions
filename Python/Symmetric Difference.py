# Enter your code here. Read input from STDIN. Print output to STDOUT

first_line = input()
second_line = input().split()
third_line = input()
fourth_line = input().split()

second_line = [int(i) for i in second_line]
fourth_line = [int(i) for i in fourth_line]

ans = list(set(second_line).symmetric_difference(set(fourth_line)))

ans = sorted(ans)
for i in ans:
    print(i)
