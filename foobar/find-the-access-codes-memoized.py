def answer(l):
    cnt = 0
    memo = [0] * len(l)
    for i in xrange(len(l) - 1):
        for j in xrange(i + 1, len(l)):
            if l[j] % l[i] == 0:
                memo[j] += 1
                cnt += memo[i]

    return cnt
