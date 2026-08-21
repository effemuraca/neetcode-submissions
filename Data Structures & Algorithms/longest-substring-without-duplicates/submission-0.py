from collections import defaultdict

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longest = 0
        l = 0
        counts = defaultdict(int)

        for r in range(0, len(s)):
            counts[s[r]] += 1

            while counts[s[r]] > 1:
                counts[s[l]] -= 1
                l += 1

            longest = max(longest, r - l + 1)

        return longest
