class Solution(object):
    def maximumTotalDamage(self, power):
        f = {}
        for i in power:
            if i in f:
                f[i] += i
            else:
                f[i] = i
        
        k = sorted(f.keys())
        d = [0] * len(k)
        d[0] = f[k[0]]
        
        for i in range(1, len(k)):
            t = f[k[i]]
            l, r = 0, i - 1
            j = -1
            
            while l <= r:
                m = (l + r) // 2
                if k[m] <= k[i] - 3:
                    j = m
                    l = m + 1
                else:
                    r = m - 1
            
            if j >= 0:
                t += d[j]
            
            d[i] = max(d[i - 1], t)
        
        return d[-1]
