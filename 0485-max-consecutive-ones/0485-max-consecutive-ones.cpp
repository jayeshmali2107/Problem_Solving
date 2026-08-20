class Solution {
public:
    int findMaxConsecutiveOnes(vector<int>& nums) {
        int curr = 0;
        int max_one = 0;

        for(int i = 0; i < nums.size(); i++){
            if( nums[i] == 1){
                curr++ ;

                max_one = max(max_one, curr);
            }
            else{
                curr = 0;
            }
        }

        return max_one;
    }
};