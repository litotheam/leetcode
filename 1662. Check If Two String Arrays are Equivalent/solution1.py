class Solution:
    def arrayStringsAreEqual(self, word1: list[str], word2: list[str]) -> bool:
        
        
        word1_str = ""
        word2_str = ""
        for word in word1:
            word1_str += word
        for word in word2:
            word2_str += word
        word1_len = len(word1_str)
        word2_len = len(word2_str)
        is_same = True
        if word1_len != word2_len:
            is_same = False
        else:
            for i in range(len(word1_str)):
                if word1_str[i] != word2_str[i]:
                    is_same = False
                    break
        return is_same