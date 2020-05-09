class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = []
        anagram_dict = {}
        max_index = 0
        for s in strs:
            key = ''.join(sorted(s))
            if key not in anagram_dict:
                anagram_dict[key] = max_index
                max_index += 1
                result.append([])
            result[anagram_dict[key]].append(s)

        return result        
