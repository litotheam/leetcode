# WRONG ANSWER!!!

class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        
        output = []
        p_length = len(p)
        s_length = len(s)

        if s_length < p_length:
            return [] 
        
        p_hashmap = {}
        s_hashmap = {}
        for char in p:
            p_hashmap[char] = p_hashmap.get(char, 0) + 1
        
        for i in range(s_length):
            j = i 
            copy_p_hashmap = p_hashmap.copy()
            while(copy_p_hashmap.get(s[j], 0) > 0):
                copy_p_hashmap[s[j]] -= 1
                j += 1
                if j > s_length - 1:
                    break
            if not copy_p_hashmap: 
                output.append(i)

        return output
