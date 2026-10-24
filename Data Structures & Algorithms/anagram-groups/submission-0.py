class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list) # create empty dict

        # loop through all words and sorts them into anagrams
        for word in strs:
            sorted_word = ''.join(sorted(word))
            res[sorted_word].append(word)

        # Return all values
        return list(res.values())
            