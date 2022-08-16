import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text) -> None:
        self.text = text
    
    def __repr__(self) -> str:
        return 'Sentence(%s)' % reprlib.repr(self.text)
    
    def __iter__(self):
        return (match.group() for match in RE_WORD.finditer(self.text))