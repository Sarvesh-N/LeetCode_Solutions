"""class Solution:
    def fizzBuzz(self, n: int) -> List[str]:
        str_list = [str(i) for i in range(1,n+1)]
        for i in str_list:
            i = int(i)
            if i % 3 == 0 and i % 5 == 0:
                str_list[i-1] = "FizzBuzz"
            elif i % 3 == 0:
                str_list[i-1] = "Fizz"
            elif i % 5 == 0:
                str_list[i-1] = "Buzz"
            else:
                
        return str_list"""

lis=[]
n=15
for i in range(1,n+1):
    if  i % 3 == 0 and i % 5 == 0:
        lis.append("FizzBuzz")
    elif i % 3 == 0:
        lis.append("Fizz")
    elif i % 5 == 0:
        lis.append("Buzz")
    else:
        lis.append(i)
print(lis)