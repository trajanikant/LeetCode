def xor_list(todo_list):
    temp = todo_list[:]
    for i in range(1, len(todo_list)-1):
        if temp[i-1] == temp[i+1]:
            todo_list[i] = 1
        else:
            todo_list[i] = 0

    todo_list[0] = todo_list[-1] = 0
    return todo_list


class Solution:
    def prisonAfterNDays(self, prison_cells, n):
        all_combinations = []
        temp = '1'
        while temp not in all_combinations:
            prison_cells = (xor_list(prison_cells))
            temp = ','.join(str(j) for j in prison_cells)
            if temp in all_combinations:
                break
            all_combinations.append(temp)
            temp = '1'

        diff = len(all_combinations) - all_combinations.index(temp)
        return (list(map(int, (all_combinations[(n % diff)-1].split(',')))))
