class Solution {
    public int bitwiseComplement(int n) {
        String bin_val = Integer.toBinaryString(n);
        String res = "";

        for (int i = 0; i<bin_val.length();i++){
            if (bin_val.charAt(i) == '1'){
                res += '0';
            }
            else{
                res += '1';
            }
        }
        int final_value = Integer.parseInt(res, 2);
        return final_value;
    }
}
