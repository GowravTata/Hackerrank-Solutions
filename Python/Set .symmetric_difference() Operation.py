# Enter your code here. Read input from STDIN. Print output to STDOUT

first = input()
second = set(map(int, input().split()))
third = input()
fourth = set(map(int, input().split()))

print(len(second.symmetric_difference(fourth)))
