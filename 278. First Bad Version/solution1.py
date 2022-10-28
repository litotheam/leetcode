# The isBadVersion API is already defined for you.
# def isBadVersion(version: int) -> bool:

class Solution:
    def firstBadVersion(self, n: int) -> int:
        i1 = 0
        i2 = n
        i = int((i1 + i2) / 2)
        while(1):
            if isBadVersion(i)==False:
                if isBadVersion(i+1)==True:
                    badVersion = i+1
                    break
                else:
                    i1 = i
                    i = int((i1 + i2) / 2)
            else:
                if isBadVersion(i-1)==False:
                    badVersion = i
                    break
                else:
                    i2 = i
                    i = int((i1 + i2) / 2)
        return badVersion