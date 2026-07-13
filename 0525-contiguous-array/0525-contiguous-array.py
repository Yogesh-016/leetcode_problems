class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        # Maps the running balance to the first index we saw it
        # Base case: A balance of 0 effectively happens at index -1
        first_seen = {0: -1}
        
        max_len = 0
        balance = 0
        
        for i, num in enumerate(nums):
            # Add 1 for a '1', subtract 1 for a '0'
            balance += 1 if num == 1 else -1
            
            # If we've seen this balance before, the subarray between 
            # the old index and current index has equal 0s and 1s
            if balance in first_seen:
                max_len = max(max_len, i - first_seen[balance])
            else:
                # Store only the first occurrence to maximize the subarray length
                first_seen[balance] = i
                
        return max_len