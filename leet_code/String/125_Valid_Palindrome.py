import collections
import re


class Solution:
    def isPalindrome(self, s: str) -> bool:

        if s == " ":
            return True

        new_str = ""
        for i in range(len(s)):
            if 65 <= ord(s[i]) <= 90:
                new_str += s[i].lower()
            elif 97 <= ord(s[i]) <= 122 or 48 <= ord(s[i]) <= 57:
                new_str += s[i]

        length = len(new_str)

        if length == 0:
            return True

        for i in range(length):
            if new_str[i] == new_str[length - 1 - i]:
                if (i == length - 1):
                    return True
            else:
                return False;

    def answer1(self, s: str) -> bool:
        strs= collections.deque()

        for char in s:
            if char.isalnum():
                strs.append(char.lower())

        while len(strs) > 1:
            if strs.popleft() != strs.pop():
                return False

    def answer2(self, s: str) -> bool:
        s = s.lower()
        s = re.sub('[^a-z0-9]','',s)

        return s == s[::-1]

        return True

