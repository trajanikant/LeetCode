class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        amountTable = [math.inf] * (amount+1)
        amountTable[0] = 0
        coins = [i for i in coins if i <= amount]
        for i in coins:
            amountTable[i] = 1
        
        for i in range(len(amountTable)):
            if amountTable[i] != 1:
                for j in coins:
                    if i-j >= 0:
                        amountTable[i] = min(amountTable[i], amountTable[i-j] + 1)
            # print(amountTable)
        
        return -1 if amountTable[amount] == math.inf else amountTable[amount]