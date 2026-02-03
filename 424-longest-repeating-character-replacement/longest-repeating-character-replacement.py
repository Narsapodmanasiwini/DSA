class Solution(object):
    def characterReplacement(self, s, k):
        """
        :type s: str
        :type k: int
        :rtype: int
        """
        n=len(s)
        l=0
        r=0
        ml=0
        count=0
        d={}
        while(r<n):
            if s[r] in d:
                d[s[r]]+=1
            else:
                d[s[r]]=1
            count=max(count,d[s[r]])
            while((r-l+1)-count>k):
                d[s[l]]-=1
                if(d[s[l]]==0):
                    del d[s[l]]
                l+=1
            ml=max(ml,r-l+1)
            r+=1
        return ml