class Solution(object):
    def uniqueMorseRepresentations(self, words):
        """
        :type words: List[str]
        :rtype: int
        """
        morse = [".-","-...","-.-.","-..",".","..-.","--.","....","..",".---","-.-",".-..","--","-.","---",".--.","--.-",".-.","...","-","..-","...-",".--","-..-","-.--","--.."]
        ans = []
        x = ""
        for word in words:
            for letter in word:
                x += str(morse[ord(letter) - ord("a")])
            ans.append(x)
            x = ""
        return len(set(ans))