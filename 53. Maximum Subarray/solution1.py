# kadane’s algorithm

class Solution:
    def maxSubArray(self, nums: list[int]) -> int:
        current_window_sum = 0
        current_largest = nums[0]
        for num in nums:
            current_window_sum += num
            if current_window_sum > current_largest:
                current_largest = current_window_sum
            if current_window_sum < 0:
                current_window_sum = 0
        return current_largest