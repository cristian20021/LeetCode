class Solution(object):
    def subarrays(self,arr):

        n = len(arr)
        result = []

        # Iterate over the start index of the subarray
        for i in range(n):
        
            # Iterate over the end index of the subarray,
            # starting from the start index
            for j in range(i+1, n+1):
            
                # Extract the subarray from the original array
                # and append it to the result list
                result.append(arr[i:j])

        return result

    def sumOddLengthSubarrays(self, arr):
        finn = 0
        listt = self.subarrays(arr)
        for x in listt:
            if len(x)%2!=0:
                finn+=sum(x)
        return finn
                
        