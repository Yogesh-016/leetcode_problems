class Solution:
    def reverse(self, x: int) -> int:
        
        sign = -1 if x < 0 else 1
        
        
        reversed_str = str(abs(x))[::-1]
        reversed_int = sign * int(reversed_str)
        
        
        if reversed_int < -2**31 or reversed_int > 2**31 - 1:
            return 0
            
        return reversed_int

    """def reverse(self, x: int) -> int:
        if x < 0:
            sign = -1
        else:
            sign = 1 
        x = abs(x)
        reverse = 0
        while x > 0:
            digit = x%10
            reverse = reverse * 10 + digit
            x = x // 10
        reverse = reverse * sign
        if reverse <-2*31 or reverse > 2*31 -1:
            return 0
        return reverse"""