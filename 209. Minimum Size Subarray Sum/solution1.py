# TLE

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        buff = []
        output = 10e6
        for j in range(len(nums)):
            buff.append(nums[j])
            while(sum(buff) >= target and i <= j):
                output = min(output, len(buff))
                i += 1
                buff.pop(0)

            j += 1
        
        if output == 10e6:
            output = 0
        
        return output