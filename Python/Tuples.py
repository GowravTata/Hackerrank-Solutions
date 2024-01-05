n = int(input())
integer = [int(x) for x in input().split()]
tup = tuple(integer)
print(hash(tup))
