def solution(scores):
    answer = 0

    n = len(scores)
    rank = [1] * n

    for i in range(n):
        my_score = scores[i][i]
        count_lower = 0
        count_same = 0

        for j in range(n):
            if score[j][i] < my_score:
                count_lower += 1
            elif score[j][i] == my_score:
                count_same += 1

        if count_lower == n - 1 or (count_same == 1 and scores[i][i] == max(scores[i]) or scores[i][i] == min(scores[i])):
            rank[i] = -1

    answer = []
    current_rank = 1

    for i in range(n):
        if rank[i] != -1:
            answer.append(current_rank)
            current_rank += 1

    return answer