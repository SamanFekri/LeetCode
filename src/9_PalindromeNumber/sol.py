import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0: # Because negative numbers cannot be palindromes
            return False
        if x == 0: # Because 0 is a palindrome and log10(0) is undefined
            return True
        n = int(math.log10(x) // 1 + 1) # Find the number of digits
        rx = 0 # Reversed x
        for i in range(n):
            # Get the ith digit from right from x
            xi = x // 10 ** i % 10
            # Make the n-ith digit from left in rx equal to xi
            rx += xi * 10**(n - i - 1)
        return x == rx

# Only run when is main
if __name__ == "__main__":
    inputList = [121, -121, 10, -101, 0]
    sol = Solution()
    for inputItem in inputList:
        print(sol.isPalindrome(inputItem))