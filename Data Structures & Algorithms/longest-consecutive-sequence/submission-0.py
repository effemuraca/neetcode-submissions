class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        hash_set = set(nums)
        best_streak = 0
        current_streak = 0
        for num in hash_set:
            if num - 1 not in hash_set:
                while num in hash_set:
                    current_streak += 1
                    num += 1
                if best_streak < current_streak:
                    best_streak = current_streak
                current_streak = 0
            
        return best_streak
