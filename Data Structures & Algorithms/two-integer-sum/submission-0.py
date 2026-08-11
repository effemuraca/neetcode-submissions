class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        idx = 0
        targets = {} 
        for num in nums:
            targ = target - num
            if targ in targets:
                return [targets[targ], idx]
            else:
                targets[num] = idx
                idx += 1
            