class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        count={}
        for num in arr:
            count[num]= count.get(num,0)+1
        seen=set()
        for freq in count.values():
            if freq in seen:
                return False
            seen.add(freq)
            
        return True