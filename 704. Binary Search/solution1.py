class Solution:
    def search(self, nums: list[int], target: int) -> int:
        left = 0
        right = len(nums) - 1
        output = -1
        while(left <= right):
            middle = (left + right) // 2
            if nums[middle] == target:
                output = middle
                break
            elif nums[middle] > target:
                right = middle - 1
            else: 
                left = middle + 1
        return output