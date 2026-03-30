class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # create a dictionary
        group = {}
        # loop through strs with word

        for word in strs:

        # sort the word in strs (sorted_word)
            sorted_word = "".join(sorted(word))
        # if sorted word exists in group

            if sorted_word in group:            
        # add to list 
                group[sorted_word].append(word)
        # else create new list with that word
            else:
                group[sorted_word] = [word]
        # return group values

        return list(group.values())