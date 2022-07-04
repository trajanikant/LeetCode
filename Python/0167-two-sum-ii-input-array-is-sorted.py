class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers)-1
        while left < right:
            cur = numbers[left] + numbers[right]

            if cur == target:
                return [left+1, right+1]
            elif cur < target:
                left += 1
            else:
                right -= 1