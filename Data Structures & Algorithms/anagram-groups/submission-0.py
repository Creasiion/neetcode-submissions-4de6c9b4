class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sortedValues = {}
        for word in strs:
            sortedWord = str(sorted(word))
            if sortedWord not in sortedValues:
                sortedValues[sortedWord] = [word]
            else:
                sortedValues[sortedWord].append(word)
        result = []
        for group in sortedValues.values():
            result.append(group)
        return result
        