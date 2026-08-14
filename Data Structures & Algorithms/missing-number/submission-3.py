class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        hash_set = set(nums)
        for i in range(len(nums)):
            if i not in hash_set:
                return i
        return len(nums)
            
        