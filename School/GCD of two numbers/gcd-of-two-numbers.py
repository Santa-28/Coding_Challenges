
class Solution:
    def gcd(self, a : int, b : int) -> int:
        while b:
            a,b=b,a%b
        return a
            



#{ 
 # Driver Code Starts

if __name__=="__main__":
    t = int(input())
    for _ in range(t):
        
        a = int(input())
        
        
        b = int(input())
        
        obj = Solution()
        res = obj.gcd(a, b)
        
        print(res)
        

# } Driver Code Ends