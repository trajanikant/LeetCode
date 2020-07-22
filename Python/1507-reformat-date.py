class Solution(object):
    def reformatDate(self, date):
        """
        :type date: str
        :rtype: str
        """
        mon = ['Jan', 'Feb', 'Mar', 'Apr', 'May', 'Jun',
               'Jul', 'Aug', 'Sep', 'Oct', 'Nov', 'Dec']
        date = date.replace('th', '')
        date = date.replace('st', '')
        date = date.replace('nd', '')
        date = date.replace('rd', '')
        date = date.split(' ')

        return(str(date[2]) + '-' + ('0' + str(mon.index(date[1])+1))[-2:] + '-' + (('0' + str(date[0]))[-2:]))
