class Solution:
    def isValid(self, s: str) -> bool:
        is_valid = True
        stack = []
        for i in range(len(s)):
            if s[i] == "(" or s[i] == "[" or s[i] == "{":
                stack.append(s[i])
            else: 
                if len(stack) == 0:
                    is_valid = False
                    break
                else:
                    tmp = stack.pop()
                    if tmp == "(" and s[i] != ")" or tmp == "[" and s[i] != "]" or tmp == "{" and s[i] != "}":
                        is_valid = False
                        break
        if len(stack) != 0:
            is_valid = False
                    
        return is_valid