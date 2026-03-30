class Solution:
    def isPalindrome(self, s: str) -> bool:
        # keep only char and lowercase them

        clean = ""
        for c in s:
            if c.isalnum():
                clean += c.lower()
            
        # check if the orignal == reverse
        return clean == clean[::-1]