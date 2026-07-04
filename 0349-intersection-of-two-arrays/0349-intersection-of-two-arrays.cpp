class Solution {
public:
    vector<int> intersection(vector<int>& nums1, vector<int>& nums2) {
        vector<bool> flag(1001, false);

        for (int num : nums1)
            flag[num] = true;

        vector<int> ans;

        for (int num : nums2) {
            if (flag[num]) {
                ans.push_back(num);
                flag[num] = false;
            }
        }

        return ans;
    }
};