class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word.isupper() or word.istitle() or word.islower():
            return True
        else:
            return False
