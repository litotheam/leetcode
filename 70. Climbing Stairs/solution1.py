class Solution:
    def climbStairs(self, n: int) -> int:
        if n == 1:
            first_index = 1
        elif n == 2:
            first_index = 2
        else: 
            first_index = 2
            second_index = 1
            for i in range(n-3, -1, -1):
                temp = first_index
                first_index += second_index
                second_index = temp
            print(first_index)
        return first_index

if __name__ == "__main__":
    s = Solution()
    s.climbStairs(5)
    s.climbStairs(6)
    s.climbStairs(7)