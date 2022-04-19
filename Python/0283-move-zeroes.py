class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        p1, p2 = 0, 0
        lenn = len(nums)
        while p2 < lenn:
            if nums[p1] == 0:
                # keeps increments the inner pointer till we find a good match
                while p2 <lenn and nums[p2] == 0:
                    p2 += 1
                if p2 == lenn:
                    break
                nums[p1], nums[p2] = nums[p2], nums[p1]
            # increments counter and keeps the correct pointer incremented on basis of previous pointer, else breaks
            p1 += 1
            p2 = max(p1, p2)
            if p1 == lenn:
                break
            