def twoStrings(s1, s2):
    m1 = set(s1)
    m2 = set(s2)
    if set.intersection(m1,m2):
        return "YES"
    return "NO"
 
if __name__ == '__main__':
    t = int(input())
    for _ in range(t):
        first = input()
        second = input()
        print (twoStrings(first, second))
