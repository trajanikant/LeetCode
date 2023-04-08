class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        hashMap = defaultdict(lambda: -1)
        stack, final = [], []
        
        for i in nums2:
            while stack and stack[-1] < i:
                hashMap[stack.pop()] = i
            stack.append(i)

        final = [hashMap[i] for i in nums1]
        return final