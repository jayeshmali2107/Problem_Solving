class Solution(object):
    def uniqueOccurrences(self, arr):
        d = {}
        for i in arr:
            if i in d:
                d[i] += 1
            else:
                d[i] = 1

        maxi = 0
        for _, j in d.items():
            maxi = max(j, maxi)

        ar = [0] * (maxi + 1) 

        for j in d.values():
            ar[j] += 1

        for a in ar:
            if a > 1:
                return False

        return True

        