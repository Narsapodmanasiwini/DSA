class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n=len(s)
        left=0
        right=0
        maxlen=0
        d=[-1]*256
        while(right<n):
            if (d[ord(s[right])] !=-1 and d[ord(s[right])]>=left):
                left=d[ord(s[right])]+1
            maxlen=max(maxlen,right-left+1)
            d[ord(s[right])]=right
            right+=1
        return maxlen