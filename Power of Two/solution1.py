class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        result = False
        i = 0
        while(pow(2, i) < n):
            i += 1
        if pow(2, i) == n:
            result = True
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.isPowerOfTwo(0))
    print(solution.isPowerOfTwo(1))
    print(solution.isPowerOfTwo(2))
    print(solution.isPowerOfTwo(3))
    print(solution.isPowerOfTwo(4))