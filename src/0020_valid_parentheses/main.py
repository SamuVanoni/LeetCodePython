class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        stack = []
        translation = {
            "(": ")",
            "[": "]",
            "{": "}"
        }
        
        for char in s:
            if char in translation:
                stack.append(char)
            elif char in translation.values(): # Se o caractere é um parêntese de fechamento
                if not stack or translation[stack.pop()] != char:
                    return False
            else: # Caso o caractere não seja um parêntese
                return False
        
        # Se o stack estiver vazio, todos os parênteses foram fechados corretamente
        return not stack