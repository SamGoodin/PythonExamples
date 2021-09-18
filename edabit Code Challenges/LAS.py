"""
edabit Coding Challenge Longest Alternating Substring https://edabit.com/challenge/RB6iWFrCd6rXWH3vi

Given a string of digits, return the longest substring with alternating odd/even or even/odd digits.
If two or more substrings have the same length, return the substring that occurs first. Minimum size 2 substring.
"""

class LAS:

    def __init__(self):
        pass

    def longest_substring(self, string):
        startIterator, endIterator = 0, 0
        substrings = []
        loopCond = True

        while loopCond:
            endIterator = self.recursiveSubstring(string, startIterator)
            if len(string[startIterator:endIterator]) > 1:
                substrings.append(string[startIterator:endIterator])
            if endIterator == len(string):
                loopCond = False
            else:
                startIterator = endIterator

        print("Substrings of " + string + ": " + str(substrings))

        longestSubstring = ""
        for string in substrings:
            if len(string) > len(longestSubstring):
                longestSubstring = string
        return longestSubstring

    def recursiveSubstring(self, string, iterator):
        curNum = int(string[iterator])
        if iterator == len(string) - 1:
            return iterator + 1
        else:
            nextNum = int(string[iterator+1])
            oeCur = self.isOddEven(curNum)
            oeNext = self.isOddEven(nextNum)

            if not oeCur:
                if oeNext:
                    return self.recursiveSubstring(string, iterator+1)
                elif not oeNext:
                    return iterator + 1
            elif oeCur:
                if oeNext:
                    return iterator + 1
                elif not oeNext:
                    return self.recursiveSubstring(string, iterator+1)
            else:
                return iterator

    def isOddEven(self, num):
        if num % 2 == 0:
            # even
            return True
        else:
            # odd
            return False

las = LAS()
print("The longest substring: " + las.longest_substring("123456777890"))
print("The longest substring: " + las.longest_substring("225424272163254474441338664823"))
print("The longest substring: " + las.longest_substring("594127169973391692147228678476"))
print("The longest substring: " + las.longest_substring("721449827599186159274227324466"))
