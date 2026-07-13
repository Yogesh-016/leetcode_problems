class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        # Dictionary to store the frequency of remainders
        # Base case: a prefix sum of 0 has a remainder of 0, seen once
        remainder_counts = {0: 1}
        
        current_sum = 0
        count = 0
        
        for num in nums:
            current_sum += num
            # Calculate the remainder and normalize it for negative numbers
            remainder = current_sum % k
            
            # If this remainder has been seen before, it means the subarray 
            # between the previous occurrence and the current index is divisible by k
            if remainder in remainder_counts:
                count += remainder_counts[remainder]
                remainder_counts[remainder] += 1
            else:
                remainder_counts[remainder] = 1
                
        return count