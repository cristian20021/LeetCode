class Solution:
    def getLeastFrequentDigit(self, n: int) -> int:
        s = str(n)
        smallnum = int(max(s))
        count = len(s)

        for i in s:
            temp_count = s.count(i)

            if temp_count < count or (temp_count == count and int(i) < smallnum):
                count = temp_count
                smallnum = int(i)
        return smallnum
