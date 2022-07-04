class Codec:
    def encode(self, strs: List[str]) -> str:
        """Encodes a list of strings to a single string.
        """
        self.allElements = len(strs)
        final = ''
        for i in strs:
            curLen = ('000' + str(len(i)))[-4:]
            final += curLen + i
        return final

    def decode(self, s: str) -> List[str]:
        """Decodes a single string to a list of strings.
        """
        final = []
        p1, p2 = 0, 4
        for _ in range(self.allElements):
            curLen = int(s[p1: p2])
            p1 += 4
            p2 += curLen
            final.append(s[p1:p2])
            p1 = p2
            p2 += 4
        
        return final


# Your Codec object will be instantiated and called as such:
# codec = Codec()
# codec.decode(codec.encode(strs))