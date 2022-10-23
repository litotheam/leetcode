class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        if n <= 0:
            output = False
        else:
            x = 0
            while (3**x < n):
                x += 1
            if 3**x == n:
                output = True
            else: 
                output = False
        return output
                
            