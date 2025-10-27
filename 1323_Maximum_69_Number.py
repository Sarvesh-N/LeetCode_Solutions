class Solution:
    def maximum69Number (self, num: int) -> int:
        n = str(num)
        s_list = []
        for i in n:
            s_list.append(int(i))

        if 6 in s_list:
            for i in range(len(s_list)):
                if s_list[i] == 6:
                    s_list[i] = 9
                    break
        v = "".join(str(i) for i in s_list)
        return int(v)
                    
