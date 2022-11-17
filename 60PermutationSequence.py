'''
link : https://leetcode.com/problems/permutation-sequence/

60. Permutation Sequence
Hard

3758

396

Add to List

Share
The set [1, 2, 3, ..., n] contains a total of n! unique permutations.

By listing and labeling all of the permutations in order, we get the following sequence for n = 3:

"123"
"132"
"213"
"231"
"312"
"321"
Given n and k, return the kth permutation sequence.

 

Example 1:

Input: n = 3, k = 3
Output: "213"
Example 2:

Input: n = 4, k = 9
Output: "2314"
Example 3:

Input: n = 3, k = 1
Output: "123"
 

Constraints:

1 <= n <= 9
1 <= k <= n!
'''
######################################################
'''
Recursive approach with 0th based indexing
TC : O(n^2)
SC : O(n)
'''
class Solution:
    
    def fact(self,n):
        if n==0:
            return 1
        return n*self.fact(n-1)
    
    def getPermutation(self, n: int, k: int) -> str:
        k-=1
        lstnum=[1]*n
        resstr=""
        return self.recursepermu(n,k,lstnum,resstr)
    
    def getidx(self,cnt,quo,idx,lstnum):
        if cnt==quo:
            lstnum[idx-1]=0
            #print("returning ",idx-1)
            return idx-1
        if lstnum[idx]:
            cnt+=1
            
        return self.getidx(cnt,quo,idx+1,lstnum)
            
        
    def recursepermu(self,n,k,lstnum,resstr):
        if n==0:
            return resstr
        
        fact=self.fact(n-1)
        quo=int(k/fact)
        rem=k%fact
        resstr+=str(self.getidx(-1,quo,0,lstnum)+1)
        return self.recursepermu(n-1,rem,lstnum,resstr)



#######################################################

'''
Iterative approach with 0th based indexing

TC : O(n^2)
SC :O(n)
'''

class Solution:
    def fact(self,n):
        if n==0:
            return 1
        return n*self.fact(n-1)
    
    def getPermutation(self, n: int, k: int) -> str:
        
        resstr=""
        arrlst=[1]*n
        k-=1 #following the 0th based indexing
        while n>0:
            fnm1=self.fact(n-1)
            quo=int(k/fnm1) #quothnum
            rem = k%fnm1

            i=0
            cnt=-1
            while cnt<quo:
                if arrlst[i]:
                    cnt+=1
                i+=1
                #print("i ",arrlst)
            resstr+=str(i)
            arrlst[i-1]=0
            k=rem
            n-=1
        return resstr


#######################################################

'''
TC :O(n^2)
SC : O(n)

'''

class Solution:
    def fact(self,n):
        if n==0:
            return 1
        return n*self.fact(n-1)
    
    def getPermutation(self, n: int, k: int) -> str:
        resstr=""
        lstnum=[1]*(n+1)
        
        return self.solvePerm(n,k,resstr,lstnum)
    
    def solvePerm(self,n:int,k:int,resstr,lstnum):
        if n==0:
            return resstr
        fact= self.fact(n-1)
        quo=int(k/fact)
        if k%fact:
            i=0
            cnt=0
            while cnt<(quo+1):
                i+=1
                if lstnum[i]:
                    cnt+=1
                elif lstnum[i]==0:
                    pass
            lstnum[i]=0
            resstr+=str(i)
            return self.solvePerm(n-1,k-quo*fact,resstr,lstnum)
        else:
            i=0
            cnt=0
            while cnt<quo:
                i+=1
                if lstnum[i]:
                    cnt+=1
                elif lstnum[i]==0:
                    pass
            resstr+=str(i)
            lstnum[i]=0
            print("i : ",i)
            #Do the reverse stuff
            n=len(lstnum)-1
            while(n>0):
                print("n : ", n)
                if lstnum[n]:
                    resstr+=str(n)
                n-=1
            return resstr
                

##########################################################
'''
Sol 1:

TC : O(n^2)
SC : O(n)
'''
class Solution:
    def fact(self,n):
        if n==0:
            return 1
        return n*self.fact(n-1)
    
    def getPermutation(self, n: int, k: int) -> str:
        resstr=""
        arr=[1]*(n+1)
        nn=n
        
        while nn>0:
            factnm1=self.fact(nn-1)
            quo=int(k/factnm1)
            rem=k%factnm1
            if rem!=0:
                #quo
                i=1
                cnt=0
                while True:
                    if arr[i]==1:
                        cnt+=1
                    if arr[i]==0:
                        pass
                    if cnt==quo+1:
                        break
                    i+=1
                resstr+=str(i)
                arr[i]=0
                k=k-quo*factnm1
            elif rem==0:
                i=1
                cnt=0
                while True:
                    if arr[i]==1:
                        cnt+=1
                    if arr[i]==0:
                        pass
                    if cnt==quo:
                        break
                    i+=1
                resstr+=str(i)
                arr[i]=0
                #all num should be reversed since its the last
                i=n
                while i>0:
                    if arr[i]:
                        resstr=resstr+str(i)
                    i-=1
                break
            nn-=1
       return resstr