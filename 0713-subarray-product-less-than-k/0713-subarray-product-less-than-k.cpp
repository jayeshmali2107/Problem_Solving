class Solution {
public:
    int numSubarrayProductLessThanK(vector<int>& nums, int k) {
        int i = 0 ,  j=0;
        int count = 0;
        long long prod =1;
        while(j < nums.size()) {
            prod *= nums[j];

            while(prod >= k && i <= j) {
                prod /= nums[i];
                i++;
            }

            count += (j - i + 1);
            j++;
        }

        return count;
    }
};