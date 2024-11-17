class Solution(object):
    def convertDateToBinary(self, date):
        """
        :type date: str
        :rtype: str
        """
        y, m, d = map(int, date.split('-'))
        ybin = bin(y)[2:] #[2:] = Remove '0b'
        mbin = bin(m)[2:]
        dbin = bin(d)[2:]  
        return ybin + '-' + mbin + '-' + dbin