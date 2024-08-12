class Solution:
    def numberToWords(self, num: int) -> str:
        if num == 0:    return "Zero"
        twoList = ['Zero', 'One', 'Two', 'Three', 'Four', 'Five', 'Six', 'Seven', 'Eight', 'Nine', 'Ten', 'Eleven', 'Twelve', 'Thirteen', 'Fourteen', 'Fifteen', 'Sixteen', 'Seventeen', 'Eighteen', 'Nineteen', 'Twenty']
        tenList = ['Zero', 'Ten', 'Twenty', 'Thirty', 'Forty', 'Fifty', 'Sixty', 'Seventy', 'Eighty', 'Ninety']
        def getTwo(number):
            if 0 < number <= 20:
                return twoList[number]
            else:
                tens = number // 10
                units = number % 10
                if tens != 0:
                    if units != 0:
                        return f"{tenList[tens]} {twoList[units]}" 
                    return f"{tenList[tens]}" 
                return ""

        def getThree(number):
            h = number // 100
            if h != 0:
                if number % 100 != 0:
                    return f"{twoList[h]} Hundred {getTwo(number % 100)}"
                else:
                    return f"{twoList[h]} Hundred"
            return f"{getTwo(number % 100)}"
        
        string = ('0'*12 + str(num))[-12:]
        b = getThree(int(string[:3]))
        m = getThree(int(string[3:6]))
        t = getThree(int(string[6:9]))
        f = getThree(int(string[9:12]))
        final = []
        if b is not None and b is not "":
            final.append(f'{b} Billion')
        if m is not None and m is not "":
            final.append(f'{m} Million')
        if t is not None and t is not "":
            final.append(f'{t} Thousand')
        if f is not None and f is not "":
            final.append(f'{f}')

        return " ".join(final)