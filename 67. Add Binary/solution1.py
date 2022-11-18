class Solution:
    def addBinary(self, a: str, b: str) -> str:
        result = ""
        length_a = len(a)
        length_b = len(b)
        if length_a < length_b:
            shorter_one = a
            longer_one = b  
        else:
            shorter_one = b
            longer_one = a  
        i = -1
        carry = 0
        while(i >= -len(shorter_one)):
            tmp = int(shorter_one[i]) + int(longer_one[i]) + carry
            if tmp == 0:
                result = "0" + result
                carry = 0
            elif tmp == 1:
                result = "1" + result
                carry = 0
            elif tmp == 2:
                result = "0" + result
                carry = 1
            elif tmp == 3:
                result = "1" + result
                carry = 1
            i -= 1
        
        while(i >= -len(longer_one)):
            tmp = int(longer_one[i]) + carry
            if tmp == 0:
                result = "0" + result
                carry = 0
            elif tmp == 1:
                result = "1" + result
                carry = 0
            elif tmp == 2:
                result = "0" + result
                carry = 1
            elif tmp == 3:
                result = "1" + result
                carry = 1
            i -= 1
        if carry == 1:
            result = "1" + result
        return result