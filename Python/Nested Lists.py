if __name__ == '__main__':
    all_pairs = []
    all_names = []
    all_score = []
    for _ in range(int(input())):
        name = input()
        score = float(input())
        all_pairs.append([name, score])
        all_names.append(name)
        all_score.append(score)
    score_list = list(set(all_score))
    score_list.sort()
    second_low = score_list[1]
    all_new = [pair for pair in all_pairs if pair[1] == second_low]
    all_new.sort()
    for i in all_new:
        print(i[0])
