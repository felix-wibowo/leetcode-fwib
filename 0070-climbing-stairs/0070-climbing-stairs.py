class Solution:
    def climbStairs(self, n: int) -> int:
        res = 0

        a, b = 0, 1
        for _ in range(n):
            a, b = b, a + b
        
        return b