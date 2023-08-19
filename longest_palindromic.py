class Solution:
    def longestPalindrome(self, s: str) -> str:
        def expandAroundCenter(left, right):
            while left >= 0 and right < len(s) and s[left] == s[right]:
                left -= 1
                right += 1
            return s[left + 1:right]

        longest = ""
        for i in range(len(s)):
            palindrome1 = expandAroundCenter(i, i)
            palindrome2 = expandAroundCenter(i, i + 1)
            
            if len(palindrome1) > len(longest):
                longest = palindrome1
            if len(palindrome2) > len(longest):
                longest = palindrome2
        
        return longest

# Test the solution
solution = Solution()
print(solution.longestPalindrome("babad"))  # Output: "bab" or "aba"
print(solution.longestPalindrome("cbbd"))   # Output: "bb"
