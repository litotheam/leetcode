class Solution:
    def countSubstrings(self, s: str) -> int:
        result = 0
        n = len(s)
        for i in range(len(s)):
            left_p = i
            right_p = i 
            while(left_p >= 0 and right_p <= n-1):
                if s[left_p] == s[right_p]:
                    result += 1
                    left_p -= 1
                    right_p += 1
                else: 
                    break
            left_p = i 
            right_p = i+1
            while(left_p >= 0 and right_p <= n-1):
                if s[left_p] == s[right_p]:
                    result += 1
                    left_p -= 1
                    right_p += 1
                else: 
                    break
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.countSubstrings("abc"))
