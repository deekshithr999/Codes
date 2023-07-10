'''
TC : O(N)
SC : O(1)
'''

class KGramCheck(object):
    def __init__(self):
        pass

    def kgramchecker(self, st1, st2, k):

        track1=[0]*26
        track2=[0]*26
        cnt1,cnt2=0,0

        if len(st1)!=len(st2):
            return 0

        for i in range(len(st1)):
            track1[ord(st1[i])-ord('a')] +=1
            track2[ord(st2[i])-ord('a')] +=1
        
        for i in range(26):
            if track1[i]-track2[i] <0:
                cnt2+= (track2[i] -track1[i])
            else:
                cnt1 += (track1[i]-track2[i])
        #print(cnt1, cnt2)
        if cnt1<=k: #tricky part these many letters are diff, but  each letter is cnt1 in replaced by other letter in cnt2
            return 1
        else:
            return 0


if __name__ == "__main__":
    kgcheck = KGramCheck()

    st1 = input()
    st2 = input()
    k = int(input())
    print("Is kgrams : ", kgcheck.kgramchecker(st1,st2,k))
