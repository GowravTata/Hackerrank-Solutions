# Enter your code here. Read input from STDIN. Print output to STDOUT
first = input()
s = set(map(int, input().split()))
second = input()
d = set(map(int, input().split()))
print(len(s.union(d)))
