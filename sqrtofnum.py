import math as ma


def floorSqrt(n):
    res = 1
    while res * res <= n:
        res += 1
    return res - 1

if __name__ == "__main__":
    n = 11
    print(floorSqrt(n))


# using binary Search

class Sqrt:
    def sqrt(self, n):
        low=1
        hi=n
        res= 2

        while low<=hi:
            mid=(low+hi)/2
            if mid*mid<=n:
                res=mid
                low=mid+1
            else:
                hi=mid-1
        return res
    
if __name__ == "__main__":
    n = 11232
    ma.sqrt(n)
    print(floorSqrt(n))