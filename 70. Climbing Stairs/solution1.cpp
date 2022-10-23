class Solution {
public:
    int climbStairs(int n) {
        int first_index;
        int second_index;
        int temp;
        if(n==1){
            first_index = 1;
        } else if (n==2)
        {
            first_index = 2;
        } else {
            first_index = 2;
            second_index = 1;
            for(int i=0; i<n-2; i++){
                temp = first_index;
                first_index += second_index;
                second_index = temp;
            }
        }
        return first_index;
    }
};