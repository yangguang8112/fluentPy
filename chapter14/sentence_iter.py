import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text) -> None:
        self.text = text
        self.words = RE_WORD.findall(text)

    def __len__(self):
        return len(self.words)
    
    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        return SentenceIterator(self.words)
    


class SentenceIterator:

    def __init__(self, words) -> None:
        self.words = words
        self.index = 0
    
    def __next__(self):
        try:
            word = self.words[self.index]
        except IndexError:
            raise StopIteration()
        self.index += 1
        return word
    
    def __iter__(self):
        return self