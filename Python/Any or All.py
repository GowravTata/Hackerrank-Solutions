# Enter your code here. Read input from STDIN. Print output to STDOUT
first = input()
second = input()

print(all(int(i) >= 1 for i in second.split(' ')) and any(
    str(number) == str(number)[::-1] for number in second.split(' ')))
