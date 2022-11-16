class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        element_count = {}
        threshold = len(nums) / 2
        for num in nums:
            element_count[num] = element_count.get(num, 0) + 1
            if element_count[num] > threshold:
                result = num
                break
        return result