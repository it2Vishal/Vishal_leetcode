class Solution:
    def lengthOfLongestSubstring(self, s):
        left = 0
        longest = 0
        seen = {}

        for right in range(len(s)):
            char = s[right]
            if char in seen and seen[char] >= left:
                left = seen[char] + 1
            seen[char] = right
            longest = max(longest, right - left + 1)

        return longest