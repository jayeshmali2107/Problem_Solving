class Solution:
    def numOfSubsequences(self, s: str) -> int:
        n = len(s)
        prefL = [0] * (n + 1)
        sufT = [0] * (n + 1)
        prefLC = [0] * (n + 1)
        sufCT = [0] * (n + 1)

        for i in range(n):
            prefL[i + 1] = prefL[i] + (1 if s[i] == 'L' else 0)

        for i in range(n - 1, -1, -1):
            sufT[i] = sufT[i + 1] + (1 if s[i] == 'T' else 0)

        Lcnt = 0
        base = 0
        for i in range(n):
            prefLC[i + 1] = prefLC[i]
            if s[i] == 'C':
                prefLC[i + 1] += Lcnt
                base += Lcnt * sufT[i + 1]
            if s[i] == 'L':
                Lcnt += 1

        Tcnt = 0
        for i in range(n - 1, -1, -1):
            sufCT[i] = sufCT[i + 1]
            if s[i] == 'C':
                sufCT[i] += Tcnt
            if s[i] == 'T':
                Tcnt += 1

        best = 0
        for p in range(n + 1):
            best = max(best, sufCT[p])
            best = max(best, prefL[p] * sufT[p])
            best = max(best, prefLC[p])

        return base + best
