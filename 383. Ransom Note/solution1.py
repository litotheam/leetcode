class Solution:
    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
        pool = {}
        for char in magazine:
            pool[char] = pool.get(char, 0) + 1
        result = True
        for char in ransomNote:
            if pool.get(char, 0) == 0:
                result = False
                break
            else:
                pool[char] -= 1
        return result