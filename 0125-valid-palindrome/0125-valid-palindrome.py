class Solution:
    def isPalindrome(self, s: str) -> bool:
        New=""

        for ch in s:
            if ch.isalnum():
                New+=ch.lower()
        return New == New[::-1]       