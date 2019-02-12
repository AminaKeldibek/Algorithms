class Solution(object):
    def isAlienSorted(self, words, order):
        """
        :type words: List[str]
        :type order: str
        :rtype: bool
        """
        def is_sorted(w1, w2, idx):
            if idx >= len(w1):
                return True
            if idx >= len(w2):
                return False

            if alphabet[w1[idx]] < alphabet[w2[idx]]:
                return True
            elif alphabet[w1[idx]] > alphabet[w2[idx]]:
                return False
            else:
                return is_sorted(w1, w2, idx + 1)

        alphabet = dict(zip([o for o in order], range(1, len(order) + 1)))

        for i in range(0, len(words) - 1):
            if not is_sorted(words[i], words[i + 1], 0):
                return False
        return True
        
