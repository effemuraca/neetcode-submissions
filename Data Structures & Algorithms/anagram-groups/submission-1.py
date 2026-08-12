class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        global_hash = {}
        for string in strs:
            list_string = [0] * 26
            for char in string:
                idx = ord(char) - ord('a')
                list_string[idx] += 1
            current = global_hash.get(tuple(list_string), [])
            current.append(string)
            global_hash[tuple(list_string)] = current

        return list(global_hash.values())
            

        


