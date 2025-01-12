class Solution:
    def merge(self, nums1: list[int], m: int, nums2: list[int], n: int) -> list[int]:
        """
        last index of nums1
        ---
        -1 since indexes start at 0
        this goes for last, m and n
        """
        last = m + n - 1

        # merge in reverse order
        while m > 0 and n > 0:
            if nums1[m - 1] > nums2[n - 1]:
                nums1[last] = nums1[m - 1]
                m -= 1
            else:
                nums1[last] = nums2[n - 1]
                n -= 1
            last -= 1

        """
        fill nums1 with leftover from nums2
        ---
        this edge case is when there are left over numbers in num2 which you know
        is less than the first index of nums1 when you comparing them in reverse order
        i.e. nums1 = [2,2,3,0,0,0] and nums2 = [1,5,6]
        """
        while n > 0:
            nums1[last] = nums2[n - 1]
            last, n = last - 1, n - 1

        return nums1


# Test Case
nums1 = [1, 2, 3, 0, 0, 0]
m = 3
nums2 = [2, 5, 6]
n = 3

sol = Solution()
response = sol.merge(nums1, m, nums2, n)
print(f"response: {response}")
