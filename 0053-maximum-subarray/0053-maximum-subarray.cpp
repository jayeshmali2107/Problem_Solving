class Solution {
public:
    int maxSubArray(vector<int>& nums) {
        int sum = 0;
        int Max_sum = INT_MIN;
        for(int i : nums){
            sum+= i;
            Max_sum = max(Max_sum,sum);
            if(sum<0){
                sum = 0;
            }
        }
        return Max_sum;
    }
};