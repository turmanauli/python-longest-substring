#function to get the length of the longest sub-string
def lengthOfLongestSubstring(s):
        cUn = ""
        lUn = ""
        for x in s:
                if x in cUn:
                        cUn = cUn.split(x, 2)[1]+x
                else:
                        cUn += x
                if len(cUn)>len(lUn):
                        lUn = cUn
        return len(lUn)
        
#function to generate longest sub-string        
def longestSubstring(s):
        cUn = ""
        lUn = ""
        for x in s:
                if x in cUn:
                        cUn = cUn.split(x, 2)[1]+x
                else:
                        cUn += x
                if len(cUn)>len(lUn):
                        lUn = cUn
        return len(lUn)
