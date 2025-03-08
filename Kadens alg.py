class Solution()
    def maxSubArray()
       max_current = max_global = nums[0]
       for i in nums(1,len(nums))
           max_current = max(nums[i],max_current*nums[i])
           max_global = max(max_global,max_global)
           return max_global