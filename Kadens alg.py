class Solution:
    def maxSubArray(self, nums):
        max_current = max_global = nums[0]  # Initialize with first element

        for i in range(1, len(nums)):  # Loop through the array from index 1
            max_current = max(nums[i], max_current + nums[i])  # Choose max sum
            max_global = max(max_global, max_current)  # Update max sum found so far

        return max_global  # Correctly indented (outside the loop)

# Example Usage
sol = Solution()
arr = [-2, 1, -3, 4, -1, 2, 1, -5, 4]
print(sol.maxSubArray(arr))  # Output: 6
