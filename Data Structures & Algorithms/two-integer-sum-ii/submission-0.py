class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left, right = 0, len(numbers) - 1

        while left < right:
            sum_pointers = numbers[left] + numbers[right]

            if sum_pointers < target:
                left += 1
            elif sum_pointers > target:
                right -= 1
            elif sum_pointers == target:
                return [left + 1, right + 1]
          