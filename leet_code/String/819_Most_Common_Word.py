import collections
import re
from _ast import List


class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        words = paragraph.lower()
        words = re.sub('[^a-z]',' ',words).split()
        counter = collections.Counter(words)
        for str in banned :
            del counter[str]
        print(counter)
        common = counter.most_common(1)
        return common.pop(0)[0]
    def counter(self, paragraph: str, banned: List[str]) -> str:
        words = [word for word in re.sub(r'[^\w]',' ',paragraph)
                 .lower().split()
                        if word not in banned]

        counts = collections.Counter(words)

        return counts.most_common(1)[0][0]