class Solution(object):
    def sortArray(self,nums):
        if len(nums) <= 1:
            return nums
            pivot = nums[len(nums) // 2]
            left = [x for x in nums if x < pivot]
            middle = [x for x in nums if x == pivot]
            right = [x for x in nums if x > right]

            return self.sortArray(left) + middle + self.sortArray(right)

