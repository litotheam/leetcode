class Solution:
    def hammingWeight(self, n: int) -> int:
        n_binary = bin(n)
        n_str = str(n_binary)
        return n_str.count('1')