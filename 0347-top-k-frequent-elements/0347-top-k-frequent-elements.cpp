class Solution {
public:
    vector<int> topKFrequent(vector<int>& nums, int k) {
        unordered_map<int, int> countMap;
        for(int num : nums) {
            countMap[num]++;
        }

        int n = nums.size();
        vector<vector<int>> buckets(n + 1);
        for(auto& pair : countMap) {
            int num = pair.first;
            int freq = pair.second;
            buckets[freq].push_back(num);
        }
        
        vector<int> res;
        for(int i = n; i >= 0; --i) {
            for(int num : buckets[i]) {
                res.push_back(num);
                // Stop as soon as we have k elements
                if(res.size() == k) {
                    return res;
                }
            }
        }
        
        return res;
    }
};