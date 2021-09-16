'''
edabit Code Challenge C*ns*r*d Str*ngs

Someone has attempted to censor my strings by replacing every vowel with a *, l*k* th*s. Luckily, I've been able to find the vowels that were removed.
Given a censored string and a string of the censored vowels, return the original uncensored string.

Example
uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo") ➞ "Where did my vowels go?"
uncensor("abcd", "") ➞ "abcd"
uncensor("*PP*RC*S*", "UEAE") ➞ "UPPERCASE"

Notes
The vowels are given in the correct order.
The number of vowels will match the number of * characters in the censored string.
'''


class CensoredStrings:

    def uncensor(self, string, vowels):
        censoredString = string
        for vowel in vowels:
            censoredString = censoredString.replace("*", vowel, 1)
        uncensoredString = censoredString
        return uncensoredString


cs = CensoredStrings()
print(cs.uncensor("Wh*r* d*d my v*w*ls g*?", "eeioeo"))
print(cs.uncensor("abcd", ""))
print(cs.uncensor("*PP*RC*S*", "UEAE"))

