# A straight forward solution that simply count the number of 0, 1 and 2. 
# Good at runtime, bad at memory. 

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        cnt_0 = 0
        cnt_1 = 0
        cnt_2 = 0

        for num in nums:
            if num == 0:
                cnt_0 += 1
            elif num == 1:
                cnt_1 += 1
            else:
                cnt_2 += 1
        for i in range(0, cnt_0):
            nums[i] = 0
        for i in range(cnt_0, cnt_0+cnt_1):
            nums[i] = 1
        for i in range(cnt_0+cnt_1, cnt_0+cnt_1+cnt_2):
            nums[i] = 2