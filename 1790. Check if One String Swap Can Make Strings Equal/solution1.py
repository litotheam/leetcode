class Solution:
    def areAlmostEqual(self, s1: str, s2: str) -> bool:
        diff_num = 0
        diff_indice = []
        for i in range(len(s1)):
            if s1[i] != s2[i]:
                diff_num += 1
                diff_indice.append(i)
            if diff_num > 2:
                output = False
                break
        if diff_num == 0:
            output = True
        elif diff_num == 1:
            output = False
        elif diff_num == 2:
            if s1[diff_indice[0]] == s2[diff_indice[1]] and s1[diff_indice[1]] == s2[diff_indice[0]]:
                output = True
            else:
                output = False
        return output