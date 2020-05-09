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


class SolutionTuple:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        for s in strs:
            result[tuple(sorted(s))].append(s)
        return result.values()


class SolutionCount:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        result = collections.defaultdict(list)
        for s in strs:
            count = [0] * 26
            for c in s:
                count[ord(c) - ord('a')] += 1
            result[tuple(count)].append(s)
        return result.values()
