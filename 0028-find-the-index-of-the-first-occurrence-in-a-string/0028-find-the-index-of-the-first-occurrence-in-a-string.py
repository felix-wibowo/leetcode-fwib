class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        left = 0

        for right in range(len(haystack)):
            left = right - len(needle) + 1
            print(left, right)

            if haystack[left:right + 1] == needle:
                return left

        return -1

