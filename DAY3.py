from math import gcd

class Solution:
    def gcdSum(self, nums: List[int]) -> int:
        prefixGcd = []
        maximum = 0
        for num in nums:
            maximum = max(maximum, num)
            prefixGcd.append(gcd(num, maximum))
        prefixGcd.sort()
        left = 0
        right = len(prefixGcd) - 1
        ans = 0
        while left < right:
            ans += gcd(prefixGcd[left], prefixGcd[right])
            left += 1
            right -= 1
        return ans

