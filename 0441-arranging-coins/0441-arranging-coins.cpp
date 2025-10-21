// O(logn) with Binary Search...
class Solution {
public:
    int arrangeCoins(int n) {
        int l = 0 , h = n;
        while(l <= h) {
            long mid = l + (h - l) / 2;
            if (n >= (mid * (mid + 1) / 2)) l = mid + 1;
            else h = mid - 1;
        } 
        return l - 1;
    }
};

// O(1) Solution with Math...
class Solution {
public:
    int arrangeCoins(int n) {
        return floor(-0.5 + sqrt((double)2 * n + 0.25));
    }
};