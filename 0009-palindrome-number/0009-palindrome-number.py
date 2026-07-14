class Solution:
    def isPalindrome(self, x: int) -> bool:
       x=str(x)

       return x==x[::-1] 

       # s=str(x)
       #rev=""
       # for i in s:
       #   rev=rev+i
       #return s==rev