# Another solution using sliding window
# Compared with solution1.py, this solution no longer maintains buff, which significantly reduces execution time
# Because we only need to know the sum of the buffer

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        i = 0
        j = 0
        buff_sum = 0
        buff_len = 0
        output = 10e6
        for j in range(len(nums)):
            buff_sum += nums[j]
            buff_len += 1
            while(buff_sum >= target and i <= j):
                output = min(output, buff_len)
                
                buff_sum -= nums[i]
                buff_len -= 1
                i += 1

            j += 1
        
        if output == 10e6:
            output = 0
        
        return output