class Solution(object):
    def largestGoodInteger(self, num):
        lst = []
        for i in range(len(num)-2):
            if num[i] == num[i+1] == num[i+2]:
                lst.append(int(num[i]))
        if len(lst) == 0:
            return ""
        return str(max(lst)) * 3
        