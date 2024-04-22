class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        res = ""
        lenghts = [len(s) for s in strs]
        minLen = min(lenghts)
        for i in range(minLen):
            ok = True
            c = strs[0][i]
            for s in strs:
                if s[i] != c:
                    ok = False
                    break
            if not ok:
                break
            res += c

        return res
