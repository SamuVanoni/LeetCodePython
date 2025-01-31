class Solution(object):
    def countTestedDevices(self, batteryPercentages):
        """
        :type batteryPercentages: List[int]
        :rtype: int
        """
        for i in range(len(batteryPercentages)):
            if batteryPercentages[i] > 0:
                for j in range(i+1, len(batteryPercentages)):
                    if batteryPercentages[j] > 0:
                        batteryPercentages[j] -= 1
        
        return sum(1 for x in batteryPercentages if x > 0)