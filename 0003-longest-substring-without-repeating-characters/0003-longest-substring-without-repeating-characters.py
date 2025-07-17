class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        r = ''
        n = ''
        for i in range(len(s)):
            if s[i] not in r:
                r += s[i]
            else:
                if len(n) < len(r):
                    n = ''
                    n += r
                r = r[r.find(s[i])+1:]
                r += s[i]
                    
        return max(len(r),len(n))