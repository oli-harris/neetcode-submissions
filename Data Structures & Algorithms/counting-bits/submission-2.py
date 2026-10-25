class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        power = 1

        for i in range(1, n + 1):
            # Power of twos always one bit
            if (i & (i-1) == 0):
                power = i
                output[i] = 1
            else:
                # One more bit than already computed number
                output[i] = 1 + output[i - power]

            
        return output