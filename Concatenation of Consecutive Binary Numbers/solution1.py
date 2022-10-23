class Solution:
    def concatenatedBinary(self, n: int) -> int:
        result_bin_str = ""
        
        for i in range(n):
            result_bin_str += bin(i+1)[2:]
        
        result_decimal = int(result_bin_str, 2)
        
        result_decimal %= 10**9+7
        
        return result_decimal
        