#User function Template for python3

class Solution:
    #Function to check if two arrays are equal or not.
    def check(self,A,B,N):
        
        #return: True or False
        #code here
        #One Way

        A.sort()
        B.sort()
        if(A==B):
            return 1
        else:
            return 0
        
        #Another Way
        # if(A!=B):
        #     return 1
        # A.sort()
        # B.sort()
        # for i in range(0,N):
        #     if(A[i]!=B[i]):
        #         return 1
        # return 0
        
        


#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__=='__main__':
    t=int(input())
    for tc in range(t):
        
        N=int(input())
        
        A = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        B = [int(x) for x in input().replace('  ',' ').strip().split(' ')]
        ob=Solution()
        if ob.check(A,B,N):
            print(1)
        else:
            print(0)
        
                
                
# } Driver Code Ends