class Solution:
    def canJump(self, nums: list[int]) -> bool:
        n = len(nums)
        target = n - 1

        for i in range(n-1, -1, -1):
            max_jump = nums[i]
            if max_jump + i >= target:
                target = i
        
        return target == 0


# Test Case
# nums = [2, 3, 1, 1, 4]
# nums = [2, 0]
nums = [3, 2, 1, 0, 4]

sol = Solution()
response = sol.canJump(nums)
print(response)