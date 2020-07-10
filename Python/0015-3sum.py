class Solution:
    def threeSum(self, nums):
        final_list = []
        nums.sort()
        
        for j in range(len(nums)):
            if((j>0) and (nums[j]==nums[j-1])):
                continue

            value = -nums[j]
            first = j + 1
            last = len(nums) - 1

            while first<last:
                s = nums[first] + nums[last]

                if s > value:
                    last -= 1
                    
                elif s < value:
                    first += 1

                else:
                    x = nums[j]
                    y = nums[first]
                    z = nums[last]
                    final_list.append([x,y,z])

                    while((first<last) and (nums[first]==y)):
                        first = first + 1
                    while((first<last) and (nums[last]==z)):
                        last = last - 1

        return final_list