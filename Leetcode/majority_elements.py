class Solution:
    def majorityElement(self, nums: list[int]) -> int:
        m = -1
        count = 0

        for i in nums:
            if count == 0:
                m = i

            if m == i:
                count += 1
            else:
                count -= 1

        return m




# Test Case
# nums = [3,2,3]

nums = [2,2,1,1,1,2,2]

sol = Solution()
response = sol.majorityElement(nums)
print(response)
