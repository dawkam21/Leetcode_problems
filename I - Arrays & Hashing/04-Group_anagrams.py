from collections import defaultdict


class Solution(object):
    def groupAnagrams(self, strs: list[str]) -> list[str]:
        anagram_map = defaultdict(list)

        for word in strs:
            sorted_word = "".join(sorted(word))
            anagram_map[sorted_word].append(word)

        return list(sorted(anagram_map.values()))

print(Solution.groupAnagrams(Solution, strs=["eat","tea","tan","ate","nat","bat"]))