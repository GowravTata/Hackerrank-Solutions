# Enter your code here. Read input from STDIN. Print output to STDOUT

n = int(input())
all_countries = set()
for i in range(n):
    all_countries.add(input())

print(len(all_countries))
