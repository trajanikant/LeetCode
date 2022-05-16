class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        lenn = len(nums1) - 1
        while m > 0 and n > 0:
            if nums1[m-1] > nums2[n-1]:
                nums1[lenn] = nums1[m-1]
                m -= 1
            else:
                nums1[lenn] = nums2[n-1]
                n -= 1
            lenn -= 1
        nums1[:n] = nums2[:n]