class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        word1_str = ""
        word2_str = ""
        for word in word1:
            word1_str += word
        for word in word2:
            word2_str += word
        if word1_str == word2_str:
            is_same = True
        else:
            is_same = False
        return is_same