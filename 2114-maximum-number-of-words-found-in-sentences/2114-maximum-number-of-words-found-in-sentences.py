class Solution:
    def mostWordsFound(self, sentences: list[str]) -> int:
        counter=0
        for i in range(len(sentences)):
            n=sentences[i].count(" ")+1
            if n>counter:
                counter=n
        return counter



        