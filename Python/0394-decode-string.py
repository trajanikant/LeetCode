class Solution:
    def decodeString(self, s):

        stack = []
        curNumber = 0
        curString = ''
        for curPtr in range(len(s)):
            if s[curPtr].isdigit():
                curNumber *= 10 
                curNumber += int(s[curPtr])
            elif s[curPtr] == '[':
                stack.extend([curString, curNumber])
                curString = ''
                curNumber = 0
            elif s[curPtr] == ']':
                newString = stack.pop() * curString
                curString = stack.pop() + newString
            else:
                curString += s[curPtr]
        return curString
