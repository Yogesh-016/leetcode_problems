class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip()
        match = re.match(r'^[\+\-]?\d+', s)
        if not match:
            return 0
            
        res = int(match.group(0))
        
        return max(-2**31, min(res, 2**31 - 1))