class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        #Idea: Sort words into their base chars in order 
        #i.e. a c t -> [act, cat]
        #If their sorted chars dont exist in the dict yet, add it
        groups = {}
        res = []
        for word in strs:
            base = sorted(word)
            if str(base) not in groups:
                groups[str(base)] = [word]
            else:
                groups[str(base)].append(word)
        for sublists in groups.values():
            res.append(sublists)
        return res
            

