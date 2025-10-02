class Solution {
public:
    int find(int num, vector<pair<int, int>>& v) {
        int res = -1;
        int l = 0, r = v.size() - 1;
        while (l <= r) {
            int mid = l + (r - l) / 2;
            if (v[mid].first >= num) {
                res = v[mid].second;
                r = mid - 1;
            } else {
                l = mid + 1;
            }
        }

        return res;
    }
    vector<int> findRightInterval(vector<vector<int>>& intervals) {
        vector<int> res;
        vector<pair<int, int>> v;
        int i = 0;
        for (auto el : intervals) {
            v.push_back({el[0], i});
            i++;
        }
        sort(v.begin(), v.end());
        for (auto el : intervals) {
            // We could also use lower_bound here, but I implemented the find
            // function for practice.
            res.push_back(find(el[1], v));
        }

        return res;
    }
};