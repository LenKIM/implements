class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        left = start = end = 0
        cnts = collections.Counter()
        
        for right in range (1, len(s)+1):
            cnts[s[right-1]]+=1
            max_cnt = cnts.most_common(1)[0][1]
            
            if right - left - max_cnt > k:
                cnts[s[left]]-=1
                left+=1
                
        return right - left
