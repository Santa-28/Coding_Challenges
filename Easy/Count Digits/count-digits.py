#User function Template for python3


# class Solution:
#     def evenlyDivides (self, N):
#         count=0
#         val=N
#         while N!=0:
#             rem=N%10
#             if(rem!=0 and val%rem==0):
#                 count+=1
#                 N=N//10
#         return count
class Solution:
    def evenlyDivides (self, N):
        count = 0
        n = [int(i) for i in str(N) if str(i) != '0']
        count = 0
        for i in n:
            if N % i == 0:
                count += 1
        return count
            



#{ 
 # Driver Code Starts
#Initial Template for Python 3

if __name__ == '__main__': 
    t = int (input ())
    for _ in range (t):
        N = int(input())
       

        ob = Solution()
        print(ob.evenlyDivides(N))
# } Driver Code Ends