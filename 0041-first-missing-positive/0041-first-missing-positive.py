class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        n = len(nums)
        
        # 1. Cyclic Sort: Place each number at its correct index (nums[i] should be at index nums[i] - 1)
        for i in range(n):
            # Keep swapping until the current element is in its correct position,
            # out of bounds, or a duplicate of the element at its target position.
            while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                # Swap nums[i] with the element at its target index
                correct_idx = nums[i] - 1
                nums[i], nums[correct_idx] = nums[correct_idx], nums[i]
        
        # 2. Find the first index where the value doesn't match the index + 1
        for i in range(n):
            if nums[i] != i + 1:
                return i + 1
                
        # 3. If all positions are filled correctly, the missing number is n + 1
        return n + 1