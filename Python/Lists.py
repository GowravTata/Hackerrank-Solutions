if __name__ == '__main__':
    N = int(input())
    l = []
    for _ in range(N):
        cmd = map(str, input().split())
        cmd_list = list(cmd)
        if cmd_list[0] == 'insert':
            l.insert(int(cmd_list[1]), int(cmd_list[2]))
        elif cmd_list[0] == 'print':
            print(l)
        elif cmd_list[0] == 'remove':
            l.remove(int(cmd_list[1]))
        elif cmd_list[0] == 'append':
            l.append(int(cmd_list[1]))
        elif cmd_list[0] == 'sort':
            l.sort()
        elif cmd_list[0] == 'pop':
            l.pop()
        elif cmd_list[0] == 'reverse':
            l.reverse()
