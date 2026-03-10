class Solution {
    public boolean checkDivisibility(int n) {
        int total = 0;
        int temp = n;
        int sumofn = 0;
        int productofn = 1;

        while (temp > 0){
            int last = temp % 10;
            sumofn += last;
            productofn *= last;
            temp /= 10;
        }

        int res = sumofn + productofn;

        if (n % res == 0){
            return true;
        }else{
            return false;
        }
    }
}
