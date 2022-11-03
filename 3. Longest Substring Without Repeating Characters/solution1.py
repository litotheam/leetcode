class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        i = 0
        j = 0
        longest = 0
        hashmap = {}
        s_length = len(s)
        while(j<s_length):
            if s[j] in hashmap:
                hashmap[s[j]] += 1
            else: 
                hashmap[s[j]] = 1
            if i==j:
                pass
            else:
                while(j-i+1 > len(hashmap)):
                    hashmap[s[i]] -= 1
                    if hashmap[s[i]] == 0:
                        del hashmap[s[i]]
                    i += 1
                    
            longest = max(longest, j-i+1)
            j += 1
        
        return longest