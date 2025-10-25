class Solution:
    def canBeTypedWords(self, text: str, brokenLetters: str) -> int:
        words = text.split()
        broke = list((brokenLetters))
        count = 0

        for i in words:
            if any(ch in i for ch in broke):
                pass
            else:
                count += 1
        return count  

        
