from collections import Counter
class Solution:
    def firstUniqChar(self, s: str) -> int:
        a = Counter(s)
        for key,value in a.items():
            if value == 1:
                return s.index(key)
        return -1
