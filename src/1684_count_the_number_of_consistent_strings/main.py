class Solution(object):
    def countConsistentStrings(self, allowed, words):
        """
        :type allowed: str
        :type words: List[str]
        :rtype: int
        """
        allowed_set = set(allowed)  # Converta allowed para um conjunto para buscas mais rápidas
        count = 0

        for word in words:
            if all(letter in allowed_set for letter in word):
                count += 1
        
        return count