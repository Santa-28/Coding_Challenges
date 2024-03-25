#User function Template for python3

class Solution:
    def armstrongNumber (self, n):
        sum=0
        val=n
        while(n>0):
            rem=n%10
            sum=sum+pow(rem,3)
            n//=10
        if val==sum:
            return "Yes"
        else:
            return "No"
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3
if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        n = input()
        n=int(n)
        ob = Solution()
        print(ob.armstrongNumber(n))
# } Driver Code Ends