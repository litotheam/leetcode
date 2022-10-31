class Solution:
    def plusOne(self, digits: list[int]) -> list[int]:
        i = -1
        digits_length = len(digits)
        digits[i] = digits[i] + 1
        while(digits[i]==10):
            digits[i] = 0
            if i-1+digits_length<0:
                digits = [1] + digits
                break
            else:
                digits[i-1] += 1
                i -= 1
        return digits