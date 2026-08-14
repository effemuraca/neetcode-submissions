class Solution:
    def hammingWeight(self, n: int) -> int:
        count = 0
        for i in range(32):
            if (n % 2) == 1:
                count += 1
            n = n >> 1
        return count

    def countBits(self, n: int) -> List[int]:
        res_list = []
        for i in range(n + 1):
            res_list.append(self.hammingWeight(i))
        return res_list


        