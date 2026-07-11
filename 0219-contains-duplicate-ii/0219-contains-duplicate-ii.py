class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        window = set()
        
        for i in range(len(nums)):
            # 1. If we see a number already in our window, we found a close duplicate
            if nums[i] in window:
                return True
            
            # 2. Add the current number to our window
            window.add(nums[i])
            
            # 3. If the window grows larger than k, remove the oldest element
            if len(window) > k:
                window.remove(nums[i - k])
                
        return False