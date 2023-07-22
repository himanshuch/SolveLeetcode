class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        res = defaultdict(list)
        for s in strs:
            count = [0]*26
            for c in s:
                count[ord(c)-ord('a')] +=1 #key with same count of alphabets
            #if tuple(count) not in res:
            #    res[tuple(count)] = []
            res[tuple(count)].append(s)
        return res.values()



        '''  
        ans=[]
        map ={}
        for s in strs:
            key = ''.join(sorted(s))
            if key not in map:
                map[key] = []
            map[key].append(s)
        for val in map.values():
            ans.append(val)
        return ans
        '''

        