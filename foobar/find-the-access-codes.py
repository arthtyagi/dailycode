## time complexity O(N^2)

def answer(l):
    cnt = 0
    pairs = []
    for i in range(len(l) - 2):
        for j in range(i + 1, len(l) - 1):
            if l[j] % l[i] == 0:
                pairs.append([l[i], l[j]])

    for pair in pairs:
        for k in range(pair[1] + 1, len(l)):
            if l[k] % pair[1] == 0:
                cnt += 1

    return cnt



