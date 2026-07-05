class Solution {
public:
    int strStr(string haystack, string needle) {
        int h = haystack.size();
        int n = needle.size();

        for (int i = 0; i <= h - n; i++) {
            bool isPresent = true;
            for (int j = i, k = 0; k < n; j++, k++) {
                if (haystack[j] != needle[k]) {
                    isPresent = false;
                    break;
                }
            }
            if (isPresent)
                return i;
        }

        return -1;
    }
};