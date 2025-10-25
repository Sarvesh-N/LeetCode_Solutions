class Solution:
    import string
    def maxFreqSum(self, s: str) -> int:
        chars = list(string.ascii_lowercase)
        vow_str = 'aeiou'
        conso_list = []
        for i in chars:
            if i not in vow_str:
                conso_list.append(i)
        vow_freq = {}
        conso_freq = {}

        for i in s:
            if i in vow_str:
                if i in vow_freq:
                    vow_freq[i] += 1
                else:
                    vow_freq[i] = 1
            elif i in conso_list:
                if i in conso_freq:
                    conso_freq[i] += 1
                else:
                    conso_freq[i] = 1
       

        if conso_freq:
            max_conso = max(conso_freq.values())
        else :
            max_conso = 0

        if vow_freq:
            max_vow = max(vow_freq.values())
        else :
            max_vow = 0
        return max_conso + max_vow
        
        
