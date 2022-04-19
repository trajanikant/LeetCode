class Solution:
    def findPeakElement(self, nums: List[int]) -> int:
        peakIndex = 0
        nums = [nums[0]-1] + nums + [nums[-1]-1]

        for i in range(1,len(nums)-1):
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                peakIndex = i-1
                break
        return peakIndex

