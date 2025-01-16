class Solution:
    def removeDuplicates(self, nums: list[int]) -> int:
        i = 1
        d = 1

        for j in range(1, len(nums)):
            if nums[j] == nums[j-1]:
                d += 1
            else:
                d = 1

            if d <= 2:
                nums[i] = nums[j]
                i += 1

        return i


# Test Case
nums = [1, 1, 1, 2, 2, 3]

# nums = [0,0,1,1,1,1,2,3,3]

sol = Solution()
response = sol.removeDuplicates(nums)
print(response)
