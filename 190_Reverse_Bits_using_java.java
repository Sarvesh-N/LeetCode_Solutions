class Solution {
    public int reverseBits(int n) {
        String arr = String.format("%32s", Integer.toBinaryString(n)).replace(' ', '0');
        char res[] = arr.toCharArray();

        int l = 0;
        int r = arr.length()-1;

        while (l < r){
            char temp = res[l];
            res[l] = res[r];
            res[r] = temp;
            l++;
            r--;
        }

        String val = new String(res);
        int final_value = Integer.parseUnsignedInt(val, 2);
        return final_value;

    }
}
