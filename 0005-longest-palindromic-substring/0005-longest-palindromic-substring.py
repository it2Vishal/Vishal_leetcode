class Solution:
    def longestPalindrome(self, s):
        def expand(left, right):
            # Expand outwards as long as characters match
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            # Return the valid palindromic substring
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            # Odd length palindromes (single character center, like "aba")
            p1 = expand(i, i)
            # Even length palindromes (two character center, like "abba")
            p2 = expand(i, i + 1)
            
            # Keep the longer substring
            if len(p1) > len(longest):
                longest = p1
            if len(p2) > len(longest):
                longest = p2

        return longest