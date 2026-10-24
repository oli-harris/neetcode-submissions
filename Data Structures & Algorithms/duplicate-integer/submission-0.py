class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        # Creates an empty set to put seen integers
        seen_integers = set()

        for integer in nums:
            # Integer already seen
            if integer in seen_integers:
                return True

            # Add to seen integers
            seen_integers.add(integer)

        return False