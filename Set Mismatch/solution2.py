class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        largest = max(nums)
        length = len(nums)
        
        in_nums = [False] * length
        
        for num in nums:
            if in_nums[num-1] == True:
                duplicate = num
            in_nums[num-1] = True
            
        loss = in_nums.index(False) + 1
        return [duplicate, loss]