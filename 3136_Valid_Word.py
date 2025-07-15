class Solution:
    def isValid(self, word: str) -> bool:
        conso = "bcdfghjklmnpqrstvwxyz"
        vowels = "aeiou"
        co = False
        vo = False
        for i in word:
            if i.lower() in conso:
                co = True
            elif i.lower() in vowels:
                vo = True
        return len(word)>=3 and word.isalnum() and co and vo
