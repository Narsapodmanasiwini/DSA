class Solution:
    def isTrionic(self, nums):
        n = len(nums)
        if n < 3:
            return False
        
        # Find the peak (end of first increasing sequence)
        peak = 0
        while peak < n - 1 and nums[peak] < nums[peak + 1]:
            peak += 1
        
        if peak == 0 or peak == n - 1:
            return False
        
        # Find the valley (end of decreasing sequence)
        valley = peak
        while valley < n - 1 and nums[valley] > nums[valley + 1]:
            valley += 1
        
        if valley == peak or valley == n - 1:
            return False
        
        # Check if remaining is increasing
        for i in range(valley, n - 1):
            if nums[i] >= nums[i + 1]:
                return False
        
        return True