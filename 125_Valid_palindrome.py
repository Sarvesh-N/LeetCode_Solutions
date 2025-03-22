class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.replace(" ","")
        out = ""

        for i in s:
            if i.isalnum():
                out+=i
        return out.lower() == out[::-1].lower()