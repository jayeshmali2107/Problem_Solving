class Solution {
public:
    int reverse(int x) {
        long long ans = 0;  
        while (x != 0) {
            int digit = x % 10;
            ans = ans * 10 + digit;
            x /= 10;

            
            if (ans > 2147483647 || ans < -2147483648) {
                return 0;
            }
        }
        return (int)ans;
    }
};