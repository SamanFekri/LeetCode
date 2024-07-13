class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        lh = len(haystack)
        ln = len(needle)
        for i in range(0, lh - ln + 1):
            if haystack[i] != needle[0]:
                continue
            if haystack[i: i + ln] == needle:
                return i
        
        return -1

