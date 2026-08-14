class Solution:
    def reverseBits(self, n: int) -> int:
        res = 0
        for i in range(32):
            res += 2**(31 - i) * (n % 2)
            n = n >> 1
        return res
        