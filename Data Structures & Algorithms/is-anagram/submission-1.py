class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        s_frequency = {}
        t_frequency = {}

        for letter in s:
            s_frequency[letter] = s_frequency.get(letter, 0) + 1

        for letter in t:
            t_frequency[letter] = t_frequency.get(letter, 0) + 1

        print(s_frequency, t_frequency)
        return s_frequency == t_frequency
        

        