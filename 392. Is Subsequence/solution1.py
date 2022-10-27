class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        output = False
        j = 0
        if len(s) == 0:
            output = True
        else: 
            for i in range(len(t)):
                if t[i] == s[j]:
                    j += 1
                if j == len(s):
                    output = True
                    break

        return output