class Solution:
    def checkDivisibility(self, n):
        digits = [int(d) for d in str(n)]

        digit_sum = sum(digits)

        digit_product = 1
        for d in digits:
            digit_product *= d  # even if 0 is present, product becomes 0

        total = digit_sum + digit_product

        if total == 0:
            return False  # avoid division by 0

        return n % total == 0
