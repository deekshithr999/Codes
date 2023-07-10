'''
Try with powerset method as well

'''

class MinDeletionsPalin(object):
    
    def __init__ (self):
        pass

    def ispalindrome(self, st1: str):
        if len(st1) == 0 or len(st1) ==1:
            return 1
        l = 0
        r = len(st1)-1

        while l<r:
            if st1[l] != st1[r]:
                return 0
            l += 1
            r -= 1
        return 1

    def mini_deletions ( self, st1: str, orig_len: int):

        if len(st1) == 0 or len(st1) == 1:
            print("CAme")
            return orig_len - len(st1)
        if self.ispalindrome(st1):
            return orig_len-len(st1)

        else:
            mini_val = 1e7
            for i in range(0,len(st1)):
                st2 = st1[0:i] + st1[i+1:len(st1)]
                #print("st2 ", st2)
                val = self.mini_deletions(st2, orig_len)
                mini_val = min(mini_val, val)
            return mini_val
        




if __name__ == "__main__":
    st1 = input()
    mdpalin = MinDeletionsPalin()
    print("mini Required : ", mdpalin.mini_deletions(st1,len(st1)))
