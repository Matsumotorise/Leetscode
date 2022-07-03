class Solution:
    def minDeletions(self, s: str) -> int:
        
        from collections import Counter
        
        freqMap = Counter(s)
        freqs = Counter(freqMap.values())
        freqsKeys = sorted(freqs.keys())
        
        
        # Cast [1, 2, 5, 5 6] -> [1,2, 4, 5, 6]
        # If duplicate found, try to cast down a frequency
        
        
                
            
        deletions = 0
        i = 0
        while i < len(freqsKeys):
            # does current element have to be casted down?
            
            offset = 0
            while freqs[freqsKeys[i]] > 1:
                while freqs[freqsKeys[i] - offset] != 0 and freqsKeys[i] - offset > 0:
                    offset += 1
                deletions += offset
                freqs[freqsKeys[i]] -= 1
                freqs[freqsKeys[i] - offset] += 1
                
                
            i += 1
           
        print(freqs)
        return deletions
            
            
        
            
        
        
        