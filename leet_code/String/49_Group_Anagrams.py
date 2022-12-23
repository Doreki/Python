import collections
from _ast import List


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        anagrams = collections.defaultdict(list)
        print(anagrams)
        for word in strs:
            anagrams[''.join(sorted(word))].append(word)

        return list(anagrams.values())

