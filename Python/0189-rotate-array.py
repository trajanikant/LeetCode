class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        lens = len(nums)
        k = k % lens

        if k != 0:
            s, e = nums[:-k], nums[-k:]
            nums[:k], nums[k:] = e, s