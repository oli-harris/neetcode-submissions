class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequency_count = {}
        result = []

        # Count frequency of each number given
        for num in nums:
            frequency_count[num] = frequency_count.get(num, 0) + 1
        
        # Sort to find most frequent
        most_frequent = sorted(frequency_count.items(), reverse=True, key=lambda item: item[1])

        # Return k from head of list
        for i in range(k):
            result.append(most_frequent[i][0])

        return result

