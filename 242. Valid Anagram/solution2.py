# Runtime improved based on solution 1

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        result = True
        hashmap_s = {}
        hashmap_t = {}
        if len(s) != len(t):
            result = False
        else:
            for i in range(len(s)):
                if s[i] in hashmap_s:
                    hashmap_s[s[i]] += 1
                else:
                    hashmap_s[s[i]] = 1
                if t[i] in hashmap_t:
                    hashmap_t[t[i]] += 1
                else:
                    hashmap_t[t[i]] = 1
            for key in list(set(s)):
                if key not in hashmap_t:
                    result = False
                else:
                    if hashmap_s[key] != hashmap_t[key]:
                        result = False

        return result