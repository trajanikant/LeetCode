class Solution:
    def countCharacters(self, words: List[str], chars: str) -> int:
        cnt, res = Counter(chars), 0
        
        for j in range(len(words)):
            cur = Counter(words[j])
            flag = 0
            for k in range(len(words[j])):
                tmp = words[j][k]
                if cur[tmp] > cnt[tmp]:
                    flag = 1
                    break
            if flag == 0:
                res += len(words[j])
                    
            #print(cur, cnt, res)
        return res