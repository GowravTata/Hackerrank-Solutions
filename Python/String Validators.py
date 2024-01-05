if __name__ == '__main__':
    s = input()
    print(True if any(a.isalnum() for a in s) else False)
    print(True if any(a.isalpha() for a in s) else False)
    print(True if any(a.isdigit() for a in s) else False)
    print(True if any(a.islower() for a in s) else False)
    print(True if any(a.isupper() for a in s) else False)
