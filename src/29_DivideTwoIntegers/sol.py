class Solution:
    def divide(self, dividend: int, divisor: int) -> int:
        if dividend == 0:
            return 0
        # if dividend == -2147483648 and divisor == -1: # I don't know why this example of them show wrong value it could be because of int space
        #     return 2147483647
            
        # Determine the sign of the result
        sign = -1 if (dividend < 0) ^ (divisor < 0) else 1
        
        # Work with positive values
        dividend, divisor = abs(dividend), abs(divisor)
        
        # Initialize quotient
        quotient = 0
        
        # Left shift divisor until it's larger than dividend
        while dividend >= divisor:
            temp, multiple = divisor, 1
            while dividend >= (temp << 1):
                temp <<= 1
                multiple <<= 1
            # Subtract the largest shifted divisor
            dividend -= temp
            # Add the corresponding multiple to the quotient
            quotient += multiple
        
        return quotient if sign == 1 else -quotient
