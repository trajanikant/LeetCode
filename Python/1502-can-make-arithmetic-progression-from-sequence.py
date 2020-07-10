class Solution:
    def canMakeArithmeticProgression(self, arr: List[int]) -> bool:
        arr.sort()
        x = 0
        diff = arr[1] - arr[0]
        for i in range(len(arr)-1):
            temp = arr[i+1] - arr[i]
            if diff != temp:
                x = 1
                break;
        
        if x==1:
            return (False)
        else:
            return (True)