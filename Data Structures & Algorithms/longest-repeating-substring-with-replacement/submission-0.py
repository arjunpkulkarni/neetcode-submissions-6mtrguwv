class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        # store frequency of each char in current window 
        count = {}
        
        left = 0
        # track most frequent char count in window
        max_count = 0   
        res = 0

        for right in range(len(s)):
            count[s[right]] = 1 + count.get(s[right], 0)
            max_count = max(max_count, count[s[right]])

            # if window is invalid (too many replacements needed), shrink it
            while (right - left + 1) - max_count > k:
                count[s[left]] -= 1
                left += 1

            # update longest valid window size 
            res = max(res, right - left + 1)

        return res