class Solution:
    def reverse(self, x: int) -> int:
        res = 0

        if x > 0:
            while x > 0:
                res = (res * 10) + (x % 10)
                x //= 10
        else:
            x *= -1
            while x > 0:
                res = (res * 10) + (x % 10)
                x //= 10
            res *= -1

        if res > 2**31 - 1 or res < -2**31:
            return 0

        return res