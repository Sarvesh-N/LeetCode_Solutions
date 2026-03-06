class Solution {
    public int minOperations(String s) {
        int starts0 = 0;
        int starts1 = 0;

        for (int i = 0;i<s.length();i++){
            if(i % 2 == 0){
                if(s.charAt(i) == '0'){
                    starts1 ++;
                }
                else{
                    starts0++;
                }
            }
            else{
                if(s.charAt(i) == '1'){
                    starts1++;
                }
                else{
                    starts0++;
                }
            }
        }
        if (starts0 < starts1){
            return starts0;
        }
        else{
            return starts1;
        }
    }
}
