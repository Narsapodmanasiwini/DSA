class Solution(object):
    def numSubarraysWithSum(self, nums, goal):
        """
        :type nums: List[int]
        :type goal: int
        :rtype: int
        """
        def func(nums,goal):
            if(goal<0):
                return 0
            Sum=0
            count=0
            l,r=0,0
            n=len(nums)
            while(r<n):
                Sum+=nums[r]
                while (Sum>goal):
                    Sum-=nums[l]
                    l+=1
                count+=(r-l+1)
                r+=1
            return count
        return func(nums,goal)-func(nums,goal-1)