class Solution:
    def findReplaceString(self, S: str, indexes: list, sources: list, targets: list) -> str:
        result = list()
        result.append(S)
        for i,index in enumerate(indexes):
            end = index+len(sources[i])
            print(f"{i},{index},{S[index:end]},{sources[i]}")
            if S[index:end] == sources[i]:
                result.append(result[-1].replace(sources[i],targets[i],1))
                print(f'{i},{index},{sources[i]},{targets[i],}' + result[-1])
        print(result[-1])


test = Solution()
test.findReplaceString("ejvzndtzncrelhedwlwiqgdbdgctgubzczgtovufncicjlwsmfdcrqeaghuevyexqdhffikvecuazrelofjmyjjznnjdkimbklrh",
[25,35,60,77,69,79,15,19,58,92,27,64,4,11,51,7,72,67,30,0,74,98,17,85,48,32,38,62,43,2,9,55,87],
["gc","tov","vy","re","ikv","lo","dw","iqgdbd","ue","kimbk","tgu","qd","ndt","elhe","crq","zn","ec","ff","bz","ej","ua","rh","lw","jj","mfd","cz","ufn","ex","cjl","vz","cr","agh","znnj"],
["dxs","hn","vfc","wnr","tira","rko","oob","mlitiwj","zrj","onpp","ot","c","lm","hbsje","dgc","ruf","qi","h","vzn","ja","ow","te","km","imq","pia","ixp","xsod","m","eat","yf","lzu","dgy","dyrsc"])