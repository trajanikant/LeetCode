def firstBadVersion(n: int) -> int:
    lo, hi = 0, n
    while hi - lo != 1:
        mid = (lo + hi) // 2
        if isBadVersion(mid) is True:
            hi = mid
        else:
            lo = mid
        print(lo, mid, hi)
    
    return hi

def isBadVersion(val):
    final = [0,0,0,0,0,0,0,1,1]
    return final[val] == 1


print(firstBadVersion(8))