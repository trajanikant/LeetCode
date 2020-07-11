class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        all_combinations = []
        final_list = []
        
        for i in range(len(nums)+1):
            all_combinations.append([list(i) for i in itertools.combinations(nums, i)])
        
        for i in range(len(nums)+1):
            for j in range(len(all_combinations[i])):
                final_list.append(all_combinations[i][j])
        
        return(final_list)