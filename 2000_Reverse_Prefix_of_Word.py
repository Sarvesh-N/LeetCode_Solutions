class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if ch not in word:
            return word
        idx = word.index(ch)
        new = list(word[:idx+1])
        last = word[idx+1:]
        left = 0
        right = len(new) - 1

        while left <= right:
            new[left], new[right] = new[right], new[left]
            left+=1
            right-=1
        new = "".join(new)
        return new + last
