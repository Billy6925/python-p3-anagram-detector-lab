# your code goes here!
class Anagram:
    def __init__(self,word):
        self.word =word
    def match(self,word):
        sorted_word = sorted(self.word)
        return ([w for w in word if sorted(w) == sorted(self.word)])