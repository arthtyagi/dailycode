def solution(start, length):
    checksum = 0
    cur = start
    cur_len = length
    while cur_len > 0:
        checksum ^= xorsum(cur) ^ xorsum(cur + cur_len)
        cur += length
        cur_len -= 1

    return checksum

def xorsum(n):
    """
    Return 0^1^2^....^(n-1)
    """
    if n == 0:
        return 0

    if (n-1) % 4 == 0:
        return n-1
    elif (n-1) % 4 == 1:
        return 1
    elif (n-1) % 4 == 2:
        return n
    else:
        return 0

## The key idea is how to find the xor sum from a to b, i.e. s(a,b)=a⊕(a+1)⊕⋯⊕(b−1)

## Time Complexity : O(1)

## if a=0 or a=1, it can be solved in O(1)

## Reference : https://www.geeksforgeeks.org/calculate-xor-1-n/ 

## s(a,b)=s(1,a)⊕s(1,b)" '
