class Solution:
    def pivotIndex(self, nums):
        totalsum =sum(nums)
        right =totalsum
        left=0
        for i in range(len(nums)):
            number =nums[i]
            right -= number
            if left == right:
                return i
            left += number
        return -1
