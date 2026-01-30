class Solution:
    def reverseArray(self, arr):
        n=len(arr)-1
        for i in range (len(arr)//2):
            arr[i],arr[n-i]=arr[n-i],arr[i]
        return arr
        
        
        
