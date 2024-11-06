class Solution(object):
    def matchPlayersAndTrainers(self, players, trainers):
        """
        :type players: List[int]
        :type trainers: List[int]
        :rtype: int
        """
        ans = 0
        players.sort()
        trainers.sort()
        for p in players:
            for t in trainers:
                if p <= t:
                    ans += 1
                    trainers.remove(t)
                    break
        return ans