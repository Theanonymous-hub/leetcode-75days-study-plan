class Solution:
    def runningSum(self, nums):
        a =0
        lst =[]
        for i in nums:
            a =i + a
            lst.append(a)
        return(lst)
