class Solution(object):
    def sortArrayByParityII(self, nums):
        odd = []
        even = []
        new_arr = []
        for i in nums:
            if i%2 == 0:
                even.append(i)
            else:
                odd.append(i)


        for j, x in zip(odd, even):
            new_arr.append(x)
            new_arr.append(j)

        return new_arr