class Solution:
    def isValid(self, s: str) -> bool:
        hashMap = dict({')':'(', '}':'{', ']':'['})
        
        st = []
        for i in s:
            if len(st):
                if i in hashMap and st[-1] == hashMap[i]:   st.pop()
                else:                                       st.append(i)
            else:
                st.append(i)
        
        return False if st else True