class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        hashmap = {}
        result = False
        for num in nums:
            hashmap[num] = hashmap.get(num, 0) + 1
            if hashmap[num] == 2:
                result = True
                break
        return result