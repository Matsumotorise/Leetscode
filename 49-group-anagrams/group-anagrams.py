import collections
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Thoughts:
        # strs -> [a:3, b:5, ...] -> (hash via tupples) -> with the hash map to an array
        results = collections.defaultdict(list)

        for s in strs:
            freqMap = [0] * 26
            for c in s:
                freqMap[ord(c)- ord('a')] +=1
            results[tuple(freqMap)].append(s)

        return results.values()





        


       