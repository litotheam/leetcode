class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        for i1 in range(len(nums)):
            remain = target - nums[i1]                
            
            if remain == nums[i1]: 
                if nums.count(remain) > 1:
                    nums.remove(nums[i1])
                    i2 = nums.index(remain) + 1
                    break
            else:
                if remain in nums:
                    i2 = nums.index(remain)
                    break
        indice = [i1, i2]
        return indice

if __name__ == "__main__":
    solution = Solution()
    print(solution.twoSum([1, 2, 3], 3))
    print(solution.twoSum([1, 23, 34], 57))
    print(solution.twoSum([1, 2, 3, 50, 40, 50], 100))