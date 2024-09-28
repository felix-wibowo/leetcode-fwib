class Solution:
    def mergeAlternately(self, word1: str, word2: str) -> str:
        min_len = min(len(word1), len(word2))

        res = ""
        for i in range(0, min_len):
            res += word1[i] + word2[i]

        if len(word1) > min_len:
            res += word1[min_len:]
        
        if len(word2) > min_len:
            res += word2[min_len:]

        return res