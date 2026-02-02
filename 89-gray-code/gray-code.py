class Solution:
    def grayCode(self, n: int) -> List[int]:
        if n == 0:
            return [0]
        
        res = self.grayCode(n - 1)
        return res + [x + (1 << (n - 1)) for x in reversed(res)]
        