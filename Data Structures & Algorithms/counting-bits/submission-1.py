class Solution:
    def countBits(self, n: int) -> List[int]:
        output = [0] * (n + 1)
        power = 1

        for i in range(1, n + 1):
            # Handle power of twos
            if (i & (i-1) == 0):
                power = i
                output[i] = 1
            else: 
                output[i] = 1 + output[i - power]

            
        return output