from itertools import combinations
def solution(L):
	L.sort(reverse = True)
	for a in reversed(range(1, len(L) + 1)):
		for tuple in combinations(L, a):
			if sum(tuple) % 3 == 0: return int(''.join(map(str, tuple)))
	return 0
