class Solution(object):
    def shortestToChar(self, s, c):
        indices = [i for i, val in enumerate(s) if val == c]
        fin = []
        for j in range(len(s)):
                minn = 999 
                for x in indices:
                    if abs(j-x) < minn:
                        minn = abs(j-x)

                fin.append(minn)     
        return fin