class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       if len(s) != len(t):
            return False
       for n in set(s):
            if s.count(n) == t.count(n):
                continue
            else:
                return False
       return True