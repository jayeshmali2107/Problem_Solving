class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = {}
        for s in strs:
            ss = ''.join(sorted(s))
            if ss in res:
                res[ss].append(s)
            else:
                res[ss] = [s]
        return list(res.values())