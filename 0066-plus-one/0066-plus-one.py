class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        num=""
        for digit in digits:
            num+=str(digit)
        num=int(num)+1
        result=[]

        for digit in str(num):
            result.append(int(digit))
        return result    
