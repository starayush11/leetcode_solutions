class Solution:
    def findNumbers(self, nums: List[int]) -> int:

        evn=0
        for num in nums:
            if len(str(num))%2==0:
                evn+=1
        return evn
