# This solution is objected due to Time Limit Exceeded
# Not fully validated but it should work
class Solution:
    def findErrorNums(self, nums: list[int]) -> list[int]:
        largest = max(nums)
        length = len(nums)
        if largest < length:
            loss = largest + 1
            for num in nums:
                if nums.count(num) == 2:
                    duplicate = num
        
        else: 
            for i in range(largest):
                num = i + 1
                if nums.count(num) == 2:
                    duplicate = num
                if num not in nums:
                    loss = num
        return [duplicate, loss]