"""
Problem     : 0215. Kth Largest Element in an Array
Link        : https://leetcode.com/problems/kth-largest-element-in-an-array/description/
Difficulty  : Medium
Topics      : Array, Divide and Conquer, Sorting, Heap (Priority Queue), Quickselect

3 months    : 
6 months    : 
>6 months   : 

Similar Qs  :
Wiggle Sort II (https://leetcode.com/problems/wiggle-sort-ii/),
Top K Frequent Elements (https://leetcode.com/problems/top-k-frequent-elements/),
Third Maximum Number (https://leetcode.com/problems/third-maximum-number/),
Kth Largest Element in a Stream (https://leetcode.com/problems/kth-largest-element-in-a-stream/),
K Closest Points to Origin (https://leetcode.com/problems/k-closest-points-to-origin/)

Time Taken  : N/A
Date        : 2026-03-31 00:21:47
Revision    : N
"""


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        heap = nums[:k]
        heapq.heapify(heap)
        lens = len(nums)
        for index in range(k, lens):
            heapq.heappush(heap, nums[index])
            heapq.heappop(heap)
        
        return heap[0]
