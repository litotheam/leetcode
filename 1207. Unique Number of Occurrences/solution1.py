class Solution:
    def uniqueOccurrences(self, arr: list[int]) -> bool:
        occurrences = {}
        out = True
        for i in range(len(arr)):
            if arr[i] not in occurrences:
                occurrences[arr[i]] = 1
            else:
                occurrences[arr[i]] += 1
        
        vals = list(occurrences.values())
        vals.sort()
        for i in range(len(vals)-1):
            if vals[i] == vals[i+1]:
                out = False
        return out
            