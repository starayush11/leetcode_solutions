class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        exp_sum=n*(n+1)//2
        act_sum=sum(nums)
        missing_num=exp_sum-act_sum
        return missing_num