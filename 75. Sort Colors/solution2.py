# This solution only needs one iteration so Space Complexity is O(n)

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left_p = 0
        iter_p = 0
        right_p = len(nums)-1
        while(iter_p <= right_p):
            if nums[iter_p] == 0:
                nums[iter_p], nums[left_p] = nums[left_p], nums[iter_p]
                iter_p += 1
                left_p += 1
            elif nums[iter_p] == 1:
                iter_p += 1
            else:
                nums[iter_p], nums[right_p] = nums[right_p], nums[iter_p]
                right_p -= 1