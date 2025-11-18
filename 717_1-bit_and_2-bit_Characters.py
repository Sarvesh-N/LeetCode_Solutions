class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0

        while i < len(bits) -1:
            if bits[i] == 0:
                i += 1
            elif bits[i] == 1:
                i += 2

        if i == len(bits) - 1:
            return True
        else:
            return False
