class Solution(object):
    def divideString(self, s, k, fill):
        remaining = k - len(s)%k
        fin = []
        for i in range(0,len(s),k):
            print(s[i:i+k])
            fin.append(s[i:i+k])
        if len(fin[-1])<k:
            toFill = k-len(fin[-1])
            for j in range(len(fin[-1]),k):
                fin[-1]+=fill
        return fin 

        