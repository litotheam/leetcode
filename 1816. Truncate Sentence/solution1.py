class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        if k == s.count(" ") + 1:
            result = s
        else:
            number_of_spaces = 0
            for i in range(len(s)):
                if s[i] == " ":
                    number_of_spaces += 1
                if number_of_spaces == k:
                    last_index = i
                    break
            result = s[:last_index]
        return result

if __name__ == "__main__":
    solution = Solution()
    print(solution.truncateSentence("Hello how are you Contestant", k=4))
    print(solution.truncateSentence("What is the solution to this problem", 4))
    print(solution.truncateSentence("chopper is not a tanuki", 5))