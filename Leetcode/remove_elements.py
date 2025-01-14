class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:      
        k = 0
        n = len(nums)
        
        while k < n:
            if nums[k] == val:
                nums[k] = nums[n-1]
                n -= 1
            else:
                k += 1

        return k


# Test Case
# nums = [3,2,2,3]
# val = 3

nums = [0,1,2,2,3,0,4,2]
val = 2

sol = Solution()
response = sol.removeElement(nums, val)
print(response)
