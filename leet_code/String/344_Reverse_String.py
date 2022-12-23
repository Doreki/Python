from _ast import List


class Solution:
    def reverseString(self, s: List[str]) -> None:
        rev_s = s[::-1]
        for i in enumerate(s):
            s[i] = rev_s[i]

    def two_pointer(self,s:List[str]) -> None:
        left, right = 0, len(s) - 1
        while left < right:
            s[left], s[right] = s[right], s[left]
            left += 1
            right -= 1

    def python_way(self,s:List[str]) -> None:
        s.reverse()

