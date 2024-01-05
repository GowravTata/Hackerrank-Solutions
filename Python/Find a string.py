def count_substring(string, sub_string):
    counter = 0
    for i in range(0, len(string)):
        for j in range(1, len(string) + 1):
            if string[i:j] == sub_string:
                counter += 1
    return counter
