class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        s_set = Counter(list(s))
        t_set = Counter(list(t))

        for ch in t_set:
            if ch not in s_set:
                return ch

            if s_set[ch] != t_set[ch]:
                return ch