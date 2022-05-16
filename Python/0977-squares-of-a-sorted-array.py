class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
#         def binarySearch(data, val):
#             lo, hi = 0, len(data) - 1
#             best_ind = lo
#             while lo <= hi:
#                 mid = lo + (hi - lo) // 2
#                 if data[mid] < val:
#                     lo = mid + 1
#                 elif data[mid] > val:
#                     hi = mid - 1
#                 else:
#                     best_ind = mid
#                     break
#                 # check if data[mid] is closer to val than data[best_ind] 
#                 if abs(data[mid] - val) < abs(data[best_ind] - val):
#                     best_ind = mid
#             return best_ind
        
#         loc = binarySearch(nums, 0)
#         print(loc)
        
        lenn = len(nums)
        i, j = 0, lenn-1
        final = [0] * lenn
        while i <= j:
            lenn -= 1
            if abs(nums[i]) > abs(nums[j]):
                cur = nums[i]
                i += 1
            else:
                cur = nums[j]
                j -= 1

            final[lenn] = cur ** 2
        
        return final