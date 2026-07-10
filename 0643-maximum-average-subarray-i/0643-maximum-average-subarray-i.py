class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        # 1. Get the sum of the very first window of size k
        current_sum = sum(nums[:k])
        maxi = current_sum

        # 2. Slide the window across the rest of the array
        for i in range(k, len(nums)):
            # Fix 1: Use += to update the running sum properly
            current_sum += nums[i] - nums[i - k]
            maxi=max(current_sum,maxi)

        # Fix 2: Use float division / instead of floor division //
        return maxi / k